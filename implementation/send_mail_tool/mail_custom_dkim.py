import json
import smtplib
import sys
from email.message import EmailMessage
import dkim

def load_json(path):
    with open(path, "r") as f:
        return json.load(f)

def build_message(cfg):
    msg = EmailMessage()

    for header, value in cfg["headers"].items():
        msg[header.title()] = value

    body = cfg.get("body", {})
    if "text" in body:
        msg.set_content(body["text"])
    if "html" in body:
        msg.add_alternative(body["html"], subtype="html")

    return msg


def dkim_sign_message(msg_bytes, dkim_cfg):
    with open(dkim_cfg["private_key"], "rb") as f:
        privkey = f.read()

    sig = dkim.sign(
        msg_bytes,
        selector=dkim_cfg["selector"].encode(),
        domain=dkim_cfg["domain"].encode(),
        privkey=privkey,
        include_headers=[b"from", b"to", b"subject"]
    )

    signed = sig + msg_bytes

    if dkim_cfg.get("break_signature"):
        signed = signed.replace(b"Subject:", b"Subject: BROKEN ", 1)

    return signed


def send_mail(cfg):
    msg = build_message(cfg)
    msg_bytes = msg.as_bytes()

    dkim_cfg = cfg.get("dkim", {})
    if dkim_cfg.get("enabled"):
        msg_bytes = dkim_sign_message(msg_bytes, dkim_cfg)

    smtp_cfg = cfg["smtp"]
    env = cfg["envelope"]

    with smtplib.SMTP(smtp_cfg["host"], smtp_cfg["port"]) as smtp:
        smtp.sendmail(
            env["mail_from"],
            env["rcpt_to"],
            msg_bytes
        )


if __name__ == "__main__":
    print("If not, turn off openDKIM for this script")
    print("sudo systemctl stop opendkim")

    if len(sys.argv) != 2:
        print("Usage: python mail_custom_dkim.py <mail.json>")
        sys.exit(1)

    config = load_json(sys.argv[1])
    send_mail(config)
    print("Mail sent successfully.")
