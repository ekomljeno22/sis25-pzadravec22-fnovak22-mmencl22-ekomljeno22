## Demonstracija odbijanja poruke koja nije prošla DMARC (dmarc=fail)

**Ubuntu**:`sudo nano /etc/opendmarc.conf`:
```
RejectFailures true
```

Na kraju: `sudo systemctl restart opendmarc`


**Ubuntu**: `sudo nano /etc/bind/db.mail-server.lab`:

Treba serial povećati za 1 i promijeniti da je u dmarc TXT zapise `p=reject`, pa `sudo systemctl restart bind9`.


Još je potrebno na Ubuntu obrisati DNS cache: `resolvectl flush-caches`.


Provjera ako se DNS promijena pohranila:
```
dig _dmarc.mail-server.lab txt
...
;; ANSWER SECTION:
_dmarc.mail-server.lab.	604800	IN	TXT	"v=DMARC1; p=quarantine; rua=mailto:reports@mail-server.lab; ruf=mailto:reports@mail-server.lab; fo=1"

```



Sada se može pokušati poslati spoofani mail:

KALI: `echo "Ovo je test za DMARC." | mail -s "DMARC test - REJECT" -r alice@mail-server.lab bob@mail-server.lab`


Sada se može vidjeti na logovima kod korisnika `alice`:

```
<bob@mail-server.lab>: host mail-server.lab[192.168.100.50] said: 550 5.7.1
    rejected by DMARC policy for mail-server.lab (in reply to end of DATA
    command)
```

Također, bob nije primio nikakav mail pa je odbijanje mailova uspješno.


## DMARC Forenzički reporti

Prikazat će se rad forenzičkih izvještaja pomoću DMARCA. Oni se temelje na DMARC TXT zapisu gdje je definirana email adresa kojoj se šalju ti izvještaji.

Primjer DNS TXT dmarc zapisa:
```
_dmarc.mail-server.lab. 604800	IN	TXT	"v=DMARC1; p=quarantine; rua=mailto:reports@mail-server.lab; ruf=mailto:reports@mail-server.lab; fo=1"
```

Ovdje je označeno `ruf=mailto:reports@mail-server.lab`, to je Reporting URI for Forensic reports i na nju se šalju DMARC izmeštaji na temelju pravila koje se nalazi u parametru `fo`.

Moguća pravila parametra `fo`:
- `fo=0`: Generira se DMARC izvještaj o neuspjehu ako i SPF i DKIM ne daju usklađeni rezultat `pass` (zadano).
- `fo=1`: Generira se DMARC izvještaj o neuspjehu ako bilo SPF ili DKIM nema usklađeni rezultat `pass` (preporučeno).
- `fo=d`: Generira se DKIM izvještaj o neuspjehu ako je potpis pao provjeru, bez obzira na usklađenost.
- `fo=s`: Generira se SPF izvještaj o neuspjehu ako SPF provjera ne uspije, bez obzira na usklađenost.


Potrebno je konfiguritati opendmarc kako bi se uključilo slanje izvještaja.


`sudo nano /etc/opendmarc.conf`:
```
FailureReports true
````



`sudo systemctl restart opendmarc`


Sada se može poslati spoofani email.

KALI: `echo "Ovo je test za DMARC." | mail -s "DMARC test - REPORTS" -r alice@mail-server.lab bob@mail-server.lab`


Primjer izvještaja koji se generirao:
```
--mail-server.lab:8922A300197
Content-Type: text/plain

This is an authentication failure report for an email message received from IP
192.168.100.10 on Mon, 12 Jan 2026 18:02:37 +0000 (UTC).

--mail-server.lab:8922A300197
Content-Type: message/feedback-report

Feedback-Type: auth-failure
Version: 1
User-Agent: OpenDMARC-Filter/1.4.2
Auth-Failure: dmarc
Authentication-Results: OpenDMARC; dmarc=fail header.from=mail-server.lab
Original-Envelope-Id: 8922A300197
Original-Mail-From: alice@mail-server.lab
Source-IP: 192.168.100.10 ([192.168.100.10])
Reported-Domain: mail-server.lab

--mail-server.lab:8922A300197
Content-Type: text/rfc822-headers

Received-SPF: Softfail (mailfrom) identity=mailfrom; client-ip=192.168.100.10; helo=kali-mail.lab; envelope-from=alice@mail-server.lab; receiver=mail-server.lab 
Received: by kali-mail.lab (Postfix, from userid 1000)
	id BA2193000EA; Mon, 12 Jan 2026 13:02:36 -0500 (EST)
Subject: DMARC test
To: <bob@mail-server.lab>
User-Agent: mail (GNU Mailutils 3.20)
Date: Mon, 12 Jan 2026 13:02:36 -0500
Message-Id: <20260112180236.BA2193000EA@kali-mail.lab>
From: alice@mail-server.lab

--mail-server.lab:8922A300197--
```








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

Ovo je **mail filter (milter)** koji:

- presreće dolazne email poruke
- analizira sadržaj i headere radi phishing znakova  
  (sumnjive riječi, linkove, obfuscaciju, HTML/JS, SPF/DKIM/DMARC)
- dodjeljuje bodove prema pronađenim indikatorima
- određuje razinu rizika (LOW → CRITICAL)
- dodaje phishing headere i predlaže akciju  
  (PASS / FLAG / QUARANTINE / REJECT)

**Svrha:** automatsko otkrivanje phishing emailova na mail serveru.

`sudo apt install -y python3.12-venv libmilter-dev build-essential`


U terminalu:
```
sudo mkdir -p /opt/phishing-milter
cd /opt/phishing-milter
```

-`sudo nano phishing_milter.py`
```
#!/usr/bin/env python3
import Milter
import re
import base64
import binascii

SOCKET = "inet:9999@127.0.0.1"

SCORE_WEIGHTS = {
    'keyword': 2,
    'suspicious_url': 3,
    'ip_in_url': 5,
    'url_shortener': 3,
    'credentials_in_url': 4,
    'suspicious_chars': 4,
    'base64_string': 3,
    'suspicious_base64': 5,
    'hex_string': 3,
    'hex_decodable': 3,
    'excessive_caps': 3,
    'exclamation': 1,
    'dmarc_fail': 10,
    'dmarc_none': 3,
    'dmarc_neutral': 2,
    'spf_fail': 8,
    'spf_none': 3,
    'spf_neutral': 2,
    'spf_softfail': 4,
    'dkim_fail': 8,
    'dkim_none': 3,
    'dkim_neutral': 2,
    'no_dkim': 5,
    'spf_mechanism_fail': 6,
    'spf_mechanism_softfail': 3,
    'spf_mechanism_neutral': 2,
    'spf_mechanism_none': 2,
    'html_js': 4,
    'homoglyph': 4,
    'dot_obfuscation': 3,
    'at_obfuscation': 3,
    'zero_width': 5,
}

PHISHING_KEYWORDS = [
    r'\bhitno\b', r'\burgent\b', r'\bimportant\b', r'\bdear customer\b',
    r'\bverify your account\b', r'\bclick here\b', r'\bpassword\b',
    r'\baccount suspended\b', r'\baccount locked\b', r'\bsecurity alert\b',
    r'\breset password\b', r'\bwire transfer\b', r'\bbank details\b',
    r'\byou won\b', r'\bprize\b', r'\blast chance\b', r'\bfinal notice\b',
]

URL_PATTERNS = [
    r'https?://\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}',
    r'hxxp[s]?://',
    r'https?://[^/\s]+@[^/\s]+',
    r'\b(bit\.ly|tinyurl\.com|goo\.gl|ow\.ly)\b',
]

SUSPICIOUS_CHAR_PATTERNS = [
    r'[\u0400-\u04FF]{3,}',
    r'[^\x00-\x7F]{4,}',
]

HTML_JS_PATTERNS = [
    r'<script[^>]*>',
    r'javascript:',
    r'on(?:click|load|mouseover)=',
    r'document\.write\s*\(',
    r'window\.open\s*\(',
    r'eval\s*\(',
    r'String\.fromCharCode\(',
    r'decodeURIComponent\s*\(',
]

HOMOGLYPH_PATTERNS = [
    r'[1l|][0oO][1l|][0oO]',
    r'[rn][nm][rn][nm]',
]

ZERO_WIDTH_CHARS = [
    '\u200b', '\u200c', '\u200d', '\ufeff', '\u2060'
]


class PhishingAnalyzer:
    
    @staticmethod
    def extract_keywords(text):
        pattern = re.compile('|'.join(PHISHING_KEYWORDS), re.IGNORECASE)
        matches = pattern.findall(text)
        return list(set([m.lower() for m in matches]))
    
    @staticmethod
    def extract_suspicious_urls(text):
        pattern = re.compile('|'.join(URL_PATTERNS), re.IGNORECASE)
        return list(set(pattern.findall(text)))
    
    @staticmethod
    def detect_suspicious_chars(text):
        pattern = re.compile('|'.join(SUSPICIOUS_CHAR_PATTERNS))
        return bool(pattern.findall(text))
    
    @staticmethod
    def detect_base64(text):
        findings = []
        b64_pattern = re.compile(r'[A-Za-z0-9+/]{20,}={0,2}')
        matches = b64_pattern.findall(text)
        
        if matches:
            findings.append(('base64_string', len(matches)))
            
            for match in matches[:2]:
                try:
                    decoded = base64.b64decode(match)
                    if len(decoded) > 10:
                        decoded_str = decoded.decode('utf-8', errors='ignore')
                        if any(keyword in decoded_str.lower() 
                               for keyword in ['http', 'click', 'login']):
                            findings.append(('suspicious_base64', 1))
                except (binascii.Error, ValueError):
                    pass
        return findings
    
    @staticmethod
    def detect_hex_encoding(text):
        findings = []
        hex_pattern = re.compile(r'(?:\\x[0-9a-fA-F]{2})+')
        matches = hex_pattern.findall(text)
        
        if matches:
            findings.append(('hex_string', len(matches)))
            
            for match in matches[:2]:
                try:
                    hex_chars = match.replace(r'\x', '')
                    decoded = bytes.fromhex(hex_chars).decode('utf-8', errors='ignore')
                    if len(decoded) > 5:
                        findings.append(('hex_decodable', 1))
                except:
                    pass
        return findings
    
    @staticmethod
    def detect_html_js(text):
        findings = []
        html_js_pattern = re.compile('|'.join(HTML_JS_PATTERNS), re.IGNORECASE)
        matches = html_js_pattern.findall(text)
        
        if matches:
            unique_matches = list(set(matches))
            findings.append(('html_js', len(unique_matches)))
            
            script_pattern = re.compile(r'<script[^>]*>([^<]+)</script>', re.IGNORECASE | re.DOTALL)
            script_matches = script_pattern.findall(text)
            
            for script in script_matches:
                if re.search(r'\\x[0-9a-fA-F]{2}', script):
                    findings.append(('hex_in_script', 1))
        
        return findings
    
    @staticmethod
    def detect_homoglyphs(text):
        findings = []
        homoglyph_pattern = re.compile('|'.join(HOMOGLYPH_PATTERNS), re.IGNORECASE)
        matches = homoglyph_pattern.findall(text)
        
        if matches:
            findings.append(('homoglyph', len(matches)))
        
        return findings
    
    @staticmethod
    def detect_zero_width_chars(text):
        findings = []
        zero_width_count = sum(1 for c in text if c in ZERO_WIDTH_CHARS)
        
        if zero_width_count > 0:
            findings.append(('zero_width', zero_width_count))
        
        return findings
    
    @staticmethod
    def detect_obfuscation(text):
        findings = []
        
        if re.search(r'\[dot\]|\(dot\)|\[\.\]|\(\.\)', text, re.IGNORECASE):
            findings.append(('dot_obfuscation', 1))
        
        if re.search(r'\[at\]|\(at\)|\[@\]|\(@\)', text, re.IGNORECASE):
            findings.append(('at_obfuscation', 1))
        
        return findings
    
    @staticmethod
    def analyze_subject(subject):
        findings = []
        
        if len(subject) > 10:
            caps_count = sum(1 for c in subject if c.isupper())
            caps_ratio = caps_count / len(subject)
            if caps_ratio > 0.5:
                findings.append(('excessive_caps', 1))
        
        exclamation_count = subject.count('!')
        if exclamation_count >= 2:
            findings.append(('exclamation', exclamation_count))
        
        return findings
    
    @staticmethod
    def analyze_dmarc(headers):
        findings = []
        
        all_headers = " ".join([f"{k}:{v}" for k, v in headers.items()]).lower()
        
        print(f"[DEBUG] Svi headeri (malim slovima): {all_headers[:500]}")
        
        dmarc_explicit = False
        
        if 'dmarc=pass' in all_headers:
            dmarc_explicit = True
            print(f"[DEBUG] Pronađen DMARC=pass")
        elif 'dmarc=fail' in all_headers:
            findings.append(('dmarc_fail', 1))
            dmarc_explicit = True
            print(f"[DEBUG] Pronađen DMARC=fail")
        elif 'dmarc=none' in all_headers:
            findings.append(('dmarc_none', 1))
            dmarc_explicit = True
            print(f"[DEBUG] Pronađen DMARC=none")
        elif 'dmarc=neutral' in all_headers:
            findings.append(('dmarc_neutral', 1))
            dmarc_explicit = True
            print(f"[DEBUG] Pronađen DMARC=neutral")
        
        has_spf_pass = False
        if 'spf=pass' in all_headers:
            has_spf_pass = True
            print(f"[DEBUG] Pronađen SPF=pass")
        elif 'spf=fail' in all_headers:
            findings.append(('spf_fail', 1))
            print(f"[DEBUG] Pronađen SPF=fail")
        elif 'spf=none' in all_headers:
            findings.append(('spf_none', 1))
            print(f"[DEBUG] Pronađen SPF=none")
        elif 'spf=neutral' in all_headers:
            findings.append(('spf_neutral', 1))
            print(f"[DEBUG] Pronađen SPF=neutral")
        elif 'spf=softfail' in all_headers:
            findings.append(('spf_softfail', 1))
            print(f"[DEBUG] Pronađen SPF=softfail")
        
        has_dkim_pass = False
        dkim_found = False
        
        if 'dkim=pass' in all_headers:
            has_dkim_pass = True
            dkim_found = True
            print(f"[DEBUG] Pronađen DKIM=pass")
        elif 'dkim=fail' in all_headers:
            findings.append(('dkim_fail', 1))
            dkim_found = True
            print(f"[DEBUG] Pronađen DKIM=fail")
        elif 'dkim=none' in all_headers:
            findings.append(('dkim_none', 1))
            dkim_found = True
            print(f"[DEBUG] Pronađen DKIM=none")
        elif 'dkim=neutral' in all_headers:
            findings.append(('dkim_neutral', 1))
            dkim_found = True
            print(f"[DEBUG] Pronađen DKIM=neutral")
        
        if not dmarc_explicit:
            print(f"[DEBUG] Nema eksplicitnog DMARC rezultata, primjenjujem pojednostavljenu logiku")
            print(f"[DEBUG] SPF pass: {has_spf_pass}, DKIM pass: {has_dkim_pass}, DKIM found: {dkim_found}")
            
            if has_spf_pass or has_dkim_pass:
                print(f"[DEBUG] DMARC se smatra PASS (ima SPF ili DKIM pass)")
                pass
            else:
                findings.append(('dmarc_none', 1))
                print(f"[DEBUG] DMARC se smatra NONE (nema SPF pass ni DKIM pass)")
        
        for key, value in headers.items():
            if 'received-spf' in key.lower():
                received_spf = value.lower()
                if 'fail' in received_spf:
                    findings.append(('spf_mechanism_fail', 1))
                elif 'softfail' in received_spf:
                    findings.append(('spf_mechanism_softfail', 1))
                elif 'neutral' in received_spf:
                    findings.append(('spf_mechanism_neutral', 1))
                elif 'none' in received_spf:
                    findings.append(('spf_mechanism_none', 1))
        
        has_dkim_sig = False
        for key in headers.keys():
            if 'dkim-signature' in key.lower():
                has_dkim_sig = True
                break
        
        if not has_dkim_sig:
            findings.append(('no_dkim', 1))
            print(f"[DEBUG] Nema DKIM-Signature headera, dodajem 'no_dkim'")
        
        elif has_dkim_sig and not dkim_found:
            findings.append(('dkim_fail', 1))
            print(f"[DEBUG] Ima DKIM potpis, ali nema DKIM rezultata, dodajem 'dkim_fail'")
        
        return findings
    
    @staticmethod
    def analyze_url_obfuscation(urls):
        findings = []
        
        for url in urls[:3]:
            encoded_count = url.count('%')
            if encoded_count > 3:
                findings.append(('excessive_url_encoding', encoded_count))
            
            double_encoded = re.search(r'%25[0-9A-F]{2}', url)
            if double_encoded:
                findings.append(('double_encoding', 1))
        
        return findings


class RiskAssessor:
    
    @staticmethod
    def calculate_score(findings):
        total_score = 0
        
        for finding_type, count in findings:
            weight = SCORE_WEIGHTS.get(finding_type, 1)
            total_score += weight * count
        
        return total_score
    
    @staticmethod
    def determine_risk_level(score):
        if score >= 25:
            return 'CRITICAL', 'REJECT'
        elif score >= 15:
            return 'HIGH', 'QUARANTINE'
        elif score >= 8:
            return 'MEDIUM', 'FLAG'
        else:
            return 'LOW', 'PASS'


class HeaderBuilder:
    
    @staticmethod
    def build_headers(score, risk_level, action, findings):
        headers = []
        
        headers.append(('X-Phishing-Score', str(score)))
        headers.append(('X-Phishing-Risk', risk_level))
        headers.append(('X-Phishing-Action', action))
        
        if findings:
            grouped = {}
            for finding_type, count in findings:
                if finding_type not in grouped:
                    grouped[finding_type] = 0
                grouped[finding_type] += count
            
            findings_list = [f"{ft}:{c}" for ft, c in grouped.items()]
            headers.append(('X-Phishing-Findings', ';'.join(findings_list[:8])))
        
        auth_findings = [f for f in findings if any(x in f[0] for x in ['dmarc', 'spf', 'dkim'])]
        if auth_findings:
            auth_list = [f"{ft}:{c}" for ft, c in auth_findings]
            headers.append(('X-Auth-Status', ';'.join(auth_list)))
        
        phishing_detected = 'true' if score >= 8 else 'false'
        headers.append(('Spam-analyse', f'phishing={phishing_detected};score={score}'))
        
        return headers


class PhishingMilter(Milter.Base):
    
    def __init__(self):
        self.subject = ''
        self.body_parts = []
        self.headers = {}
        self.analyzer = PhishingAnalyzer()
        self.risk_assessor = RiskAssessor()
        self.header_builder = HeaderBuilder()
        
    def header(self, name, value):
        name_lower = name.lower()
        self.headers[name_lower] = value
        
        if name_lower == 'subject':
            self.subject = value
        return Milter.CONTINUE

    def body(self, chunk):
        try:
            self.body_parts.append(chunk.decode('utf-8', errors='ignore'))
        except:
            self.body_parts.append(str(chunk))
        return Milter.CONTINUE

    def eom(self):
        try:
            body_text = ''.join(self.body_parts)
            full_text = f"{self.subject} {body_text}"
            
            print(f"\n[MILTER] Analyzing: {self.subject[:50]}...")
            
            findings = self._perform_all_analyses(full_text)
            
            total_score = self.risk_assessor.calculate_score(findings)
            
            risk_level, action = self.risk_assessor.determine_risk_level(total_score)
            
            headers = self.header_builder.build_headers(total_score, risk_level, action, findings)
            
            for header_name, header_value in headers:
                self.addheader(header_name, header_value)
            
            self._display_results(total_score, risk_level, action, findings)
            
            return Milter.ACCEPT
            
        except Exception as e:
            print(f"[MILTER ERROR] {e}")
            import traceback
            traceback.print_exc()
            self.addheader('X-Phishing-Error', 'analysis_failed')
            return Milter.ACCEPT
    
    def _perform_all_analyses(self, full_text):
        findings = []
        
        keywords = self.analyzer.extract_keywords(full_text)
        if keywords:
            findings.append(('keyword', len(keywords)))
            print(f"  Keywords: {', '.join(keywords[:3])}")
        
        urls = self.analyzer.extract_suspicious_urls(full_text)
        if urls:
            findings.append(('suspicious_url', len(urls)))
            for url in urls[:2]:
                print(f"  Suspicious URL: {url[:60]}")
                
                if re.search(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', url):
                    findings.append(('ip_in_url', 1))
                
                if re.search(r'bit\.ly|tinyurl', url, re.IGNORECASE):
                    findings.append(('url_shortener', 1))
                
                if '@' in url:
                    findings.append(('credentials_in_url', 1))
            
            findings.extend(self.analyzer.analyze_url_obfuscation(urls))
        
        if self.analyzer.detect_suspicious_chars(full_text):
            findings.append(('suspicious_chars', 1))
        
        findings.extend(self.analyzer.detect_base64(full_text))
        findings.extend(self.analyzer.detect_hex_encoding(full_text))
        findings.extend(self.analyzer.detect_html_js(full_text))
        findings.extend(self.analyzer.detect_homoglyphs(full_text))
        findings.extend(self.analyzer.detect_zero_width_chars(full_text))
        findings.extend(self.analyzer.detect_obfuscation(full_text))
        findings.extend(self.analyzer.analyze_subject(self.subject))
        findings.extend(self.analyzer.analyze_dmarc(self.headers))
        
        return findings
    
    def _display_results(self, score, risk_level, action, findings):
        print(f"  Score: {score} | Risk: {risk_level} | Action: {action}")
        
        if findings:
            grouped = {}
            for finding_type, count in findings:
                if finding_type not in grouped:
                    grouped[finding_type] = 0
                grouped[finding_type] += count
            
            findings_str = ';'.join([f"{ft}:{c}" for ft, c in grouped.items()][:6])
            print(f"  Findings: {findings_str}")


def main():
    print("=" * 60)
    print("PHISHING MILTER - ISPRAVLJENA LOGIKA")
    print("=" * 60)
    print(f"Listening on: {SOCKET}")
    print("=" * 60)
    
    Milter.factory = PhishingMilter
    Milter.runmilter('phishing-milter-fixed', SOCKET, timeout=60)

if __name__ == '__main__':
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
