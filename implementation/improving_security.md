## Dovecot server - filteri za dmarc=fail

Ovaj dio se odnosi na opis kako da se u aplikaciji Thunderbird složi mail filter da automatski označi dolazne mailove kao Junk kada u sebi sadrže zapis `dmarc=fail`.

Podsjetnik:
- Istiniti mail (u Kali CLI): `echo "Pozdrav LP" | mail -s "Thunderbird Test" filip@mail-server.lab`
- Spoofani mail (u Kali CLI): `echo "Pozdrav LP" | mail -s "Thunderbird Test" -r alice@mail-server.lab filip@mail-server.lab`

Može se pritisnuti tipka ALT da se pojavi izbornik (gore). Tada se ode na Tools -> Message Filters. Kada se otvori prozor, odabire se opcija `New...`. Potrebno je postaviti slijedeće opcije kao što je to prikazano na slici ispod:

<p align="center">
 <a href="https://github.com/user-attachments/assets/964373be-5459-4a4d-8acb-7cf1feea986c?raw=true" target="_blank">
  <img src="https://github.com/user-attachments/assets/964373be-5459-4a4d-8acb-7cf1feea986c"/>
  <a/>
<p/>

Zatim se pritisne tipka OK, i trebao bi se pojaviti stvoreni filter:

<p align="center">
 <a href="https://github.com/user-attachments/assets/f9d93ab7-d649-4f11-aaa6-bebab9c76f68?raw=true" target="_blank">
  <img src="https://github.com/user-attachments/assets/f9d93ab7-d649-4f11-aaa6-bebab9c76f68"/>
  <a/>
<p/>


Zatim se može odabrati stvoreni filter i pritisnuti gumb Run Now.

Sada bi Thunderbird trebao označiti spoofani mail sa oznakom Junk (mala ikona vatrice) kao što se vidi na slici:

<p align="center">
 <a href="https://github.com/user-attachments/assets/269cb912-4370-4ea4-86de-2f8fc61c85e4?raw=true" target="_blank">
  <img src="https://github.com/user-attachments/assets/269cb912-4370-4ea4-86de-2f8fc61c85e4"/>
  <a/>
<p/>

## Vlastiti Milter

`sudo apt install -y python3.12-venv libmilter-dev build-essential`


U temrinalu:
```
sudo mkdir -p /opt/phishing-milter
cd /opt/phishing-milter
```

-`sudo nano phishing_milter.py`
```
#!/usr/bin/env python3
import Milter
import re

# socket: inet:<port>@<host>
SOCKET = "inet:9999@127.0.0.1"

KEYWORDS = [
    r"\bhitno\b",
    r"dear customer",
    r"verify your account",
    r"click here",
    r"password"
]
KEYWORDS_RE = re.compile("|".join(KEYWORDS), re.IGNORECASE)

class PhishingMilter(Milter.Base):
    def __init__(self):
        self._subject = ""
        self._body = b""

    # Postfix prijeđe kroz zaglavlja ovim pozivom
    def header(self, name, value):
        if name.lower() == "subject":
            self._subject = value
        return Milter.CONTINUE

    # Tijelo maila dolazi u chunkovima
    def body(self, chunk):
        self._body += chunk
        return Milter.CONTINUE

    # End of message - radi se analiza i doda header
    def eom(self):
        text = (self._subject or "") + "\n" + self._body.decode(errors="ignore")
        phishing = bool(KEYWORDS_RE.search(text))
        header_value = f"phishing={'true' if phishing else 'false'}"
        # dodaj header; Postfix će ga vidjeti nakon prihvata
        self.addheader("Spam-analyse", header_value)
        return Milter.ACCEPT

def main():
    Milter.factory = PhishingMilter
    # ime, socket, timeout
    Milter.runmilter("phishing-milter", SOCKET, timeout=30)

if __name__ == "__main__":
    main()

```

```
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip setuptools wheel
pip install --upgrade pip 
pip install pymilter
deactivate
```

```
sudo chown -R root:root /opt/phishing-milter
sudo chmod 755 /opt/phishing-milter/phishing_milter.py
sudo chmod -R 755 /opt/phishing-milter/venv
```

-`sudo nano /etc/systemd/system/phishing-milter.service`
```
[Unit]
Description=Simple Phishing Detection Milter (inet)
After=network.target

[Service]
Type=simple
User=postfix
Group=postfix
# Pokrećemo Python iz venv-a da koristi instalirane pip pakete
ExecStart=/opt/phishing-milter/venv/bin/python /opt/phishing-milter/phishing_milter.py
Restart=on-failure
RestartSec=5

[Install]
WantedBy=multi-user.target
```

```
sudo systemctl daemon-reload
sudo systemctl enable --now phishing-milter
sudo systemctl status phishing-milter
```


- `sudo nano /etc/postfix/main.cf`:
```
smtpd_milters = local:opendkim/opendkim.sock, local:opendmarc/opendmarc.sock, inet:127.0.0.1:9999
```

`sudo systemctl restart postfix`

OD KALI: `echo "HITNO promijeni password" | mail -s "HITNO" filip@mail-server.lab`

U dolaznom mailu na Ubuntu se pojavljuje: `Spam-analyse: phishing=true`
