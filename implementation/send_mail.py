import json
import smtplib
import sys
from email.message import EmailMessage

def load_payload(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def build_message(cfg):
    msg = EmailMessage()

    msg["From"] = cfg["headers"]["From"]
    msg["To"] = cfg["headers"]["To"]
    msg["Subject"] = cfg["headers"]["Subject"]

    for h, v in cfg.get("extra_headers", {}).items():
        msg[h] = v

    msg.set_content(cfg["body"])

    return msg

def send_mail(cfg):
    msg = build_message(cfg)

    smtp_host = cfg["smtp"]["host"]
    smtp_port = cfg["smtp"].get("port", 25)

    print(f"[+] Connecting to {smtp_host}:{smtp_port}")
    with smtplib.SMTP(smtp_host, smtp_port) as server:
        server.send_message(msg)

    print("[+] Mail sent")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 send_mail.py payload.json")
        sys.exit(1)

    payload = load_payload(sys.argv[1])
    send_mail(payload)
