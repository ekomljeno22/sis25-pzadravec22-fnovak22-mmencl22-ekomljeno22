# Praktičan dio - email napadi i analiza
U ovom dijelu se rade razni napadi i testiranje servera pomoću dvije python skripte koje emuliraju slanje mail poruka, bilo to validnih ili lažiranih poruka.  

## 2.1. Slanje validne mail poruke
Za slanje validne mail poruke koja je od validnog korisnika se koristi JSON datoteka koja sadrži slijedeće podatke:  

```json
{
  "smtp": {
    "host": "kali-mail.lab"
  },
  "headers": {
    "From": "kali@kali-mail.lab",
    "To": "enjo@mail-server.lab",
    "Subject": "Legit test"
  },
  "body": "Ovo je legitiman LAB test mail."
}
```

Kada se poruka pošalje, server primi ovu poruku (preko komande mail):

```
Return-Path: <kali@kali-mail.lab>
X-Original-To: enjo@mail-server.lab
Delivered-To: enjo@mail-server.lab
Authentication-Results: OpenDMARC; dmarc=pass (p=quarantine dis=none) header.fro
m=kali-mail.lab
Authentication-Results: mail-server.lab;
    dkim=pass (2048-bit key; unprotected) header.d=kali-mail.lab header.i=@k
ali-mail.lab header.a=rsa-sha256 header.s=default header.b=UR4tn8gi;
    dkim-atps=neutral
Received-SPF: Pass (mailfrom) identity=mailfrom; client-ip=192.168.100.10; helo=
kali-mail.lab; envelope-from=kali@kali-mail.lab; receiver=mail-server.lab 
Received: from kali-mail.lab (unknown [192.168.100.10])
    by mail-server.lab (Postfix) with ESMTPS id 8B93A300197
    for <enjo@mail-server.lab>; Mon, 12 Jan 2026 18:26:46 +0000 (UTC)
Authentication-Results: OpenDMARC; dmarc=pass (p=quarantine dis=none) header.fro
m=kali-mail.lab
Authentication-Results: OpenDMARC; spf=pass smtp.mailfrom=kali-mail.lab
DKIM-Signature: v=1; a=rsa-sha256; c=relaxed/simple; d=kali-mail.lab;
    s=default; t=1768242405;
    bh=5U2tX1iP0diR8jOj+ZFibmt0zuZr83mV5EU1rTQXHMM=;
    h=From:To:Subject:Date:From;
    b=UR4tn8gigoH4c2sYLu/MBZdyNbPcfzMR7dQ0sKYXjCcSi08tKVKzU3sVU8y5YZJ4K
     9Oo+gD/UTUmVhCg6WqYxKNegmrg9wi5T4qGKVEXmGkLMQGzx+Iq/hiLiCp91Qw6mV2
     UB/kZVZN3Kszb8cUfwf6rZAVTbf89q/UX00pj5hwc/YhkXJaNMeZuT1ycoy9k/WsMF
     NCLYi2BTD6rQB7RTdyopyuQmYpIADWih++XHgGXD+tlYBDF/fQabn6+wlrci9EGJdx
     3efqzTYXuAl/TIr0sGrIz8RAgmS2mRtHnn9vwAq61BATEOZ2CVXJMRulvyiWzsTmRU
     V/cj0iLQPRFuQ==
Received: from kali-mail.lab (kali-mail.lab [192.168.100.10])
    by kali-mail.lab (Postfix) with ESMTP id 4161930008E
    for <enjo@mail-server.lab>; Mon, 12 Jan 2026 13:26:45 -0500 (EST)
From: kali@kali-mail.lab
To: enjo@mail-server.lab
Subject: Legit test
Content-Type: text/plain; charset="utf-8"
Content-Transfer-Encoding: 7bit
MIME-Version: 1.0
Message-Id: <20260112182645.4161930008E@kali-mail.lab>
Date: Mon, 12 Jan 2026 13:26:45 -0500 (EST)

Ovo je legitiman LAB test mail.
```

Vidi se kako SPF, DKIM i DMARC prolaze.

## 2.2. Slanje spoofane mail poruke
Payload spoofane poruke izgleda ovako:

```json
{
  "smtp": {
    "host": "kali-mail.lab"
  },
  "headers": {
    "From": "alice@mail-server.lab",
    "To": "bob@mail-server.lab",
    "Subject": "HITNO: Reset lozinke"
  },
  "body": "Klikni na link za reset lozinke: http://evil.lab/reset"
}

```

Poruka, kada poslana serveru, izgleda ovako:  

```
Return-Path: <alice@mail-server.lab>
X-Original-To: bob@mail-server.lab
Delivered-To: bob@mail-server.lab
Authentication-Results: OpenDMARC; dmarc=fail (p=quarantine dis=none) header.from=mail-server.lab
Authentication-Results: OpenDMARC; spf=fail smtp.mailfrom=mail-server.lab
Received: from kali-mail.lab (unknown [192.168.100.10])
	by mail-server.lab (Postfix) with ESMTPS id 1A3372A0378
	for <bob@mail-server.lab>; Mon, 12 Jan 2026 18:25:36 +0000 (UTC)
Authentication-Results: OpenDMARC; dmarc=fail (p=quarantine dis=none) header.from=mail-server.lab
Authentication-Results: OpenDMARC; spf=fail smtp.mailfrom=mail-server.lab
Received: from kali-mail.lab (kali-mail.lab [192.168.100.10])
	by kali-mail.lab (Postfix) with ESMTP id 1C538C0068
	for <bob@mail-server.lab>; Mon, 12 Jan 2026 13:25:36 -0500 (EST)
From: alice@mail-server.lab
To: bob@mail-server.lab
Subject: HITNO: Reset lozinke
Content-Type: text/plain; charset="utf-8"
Content-Transfer-Encoding: 7bit
MIME-Version: 1.0
Message-Id: <20260112182536.1C538C0068@kali-mail.lab>
Date: Mon, 12 Jan 2026 13:25:36 -0500 (EST)

Klikni na link za reset lozinke: http://evil.lab/reset
```

Budući da "from" zapis nije isti kao i "envelope" zapis, SPF pada, a ujedno pada i DKIM jer nema. Budući da i SPF i DKIM padaju, pada i DMARC.

## 2.3. Slanje phishing poruke
Kod phishinga, payload izgleda ovako:

```json
{
  "smtp": {
    "host": "kali-mail.lab"
  },
  "headers": {
    "From": "kali@kali-mail.lab",
    "To": "enjo@mail-server.lab",
    "Subject": "Sigurnosno upozorenje"
  },
  "body": "Vaš račun je zaključan.\nPotvrdite identitet slanjem lozinke."
}
```

Kod servera, poruka izgleda ovako:  

```
Return-Path: <kali@kali-mail.lab>
X-Original-To: enjo@mail-server.lab
Delivered-To: enjo@mail-server.lab
Authentication-Results: OpenDMARC; dmarc=pass (p=quarantine dis=none) header.from=kali-mail.lab
Authentication-Results: mail-server.lab;
	dkim=pass (2048-bit key; unprotected) header.d=kali-mail.lab header.i=@kali-mail.lab header.a=rsa-sha256 header.s=default header.b=CDcqPiTr;
	dkim-atps=neutral
Received-SPF: Pass (mailfrom) identity=mailfrom; client-ip=192.168.100.10; helo=kali-mail.lab; envelope-from=kali@kali-mail.lab; receiver=mail-server.lab 
Received: from kali-mail.lab (unknown [192.168.100.10])
	by mail-server.lab (Postfix) with ESMTPS id 06C3A300197
	for <enjo@mail-server.lab>; Mon, 12 Jan 2026 18:28:40 +0000 (UTC)
Authentication-Results: OpenDMARC; dmarc=pass (p=quarantine dis=none) header.from=kali-mail.lab
Authentication-Results: OpenDMARC; spf=pass smtp.mailfrom=kali-mail.lab
DKIM-Signature: v=1; a=rsa-sha256; c=relaxed/simple; d=kali-mail.lab;
	s=default; t=1768242519;
	bh=9+oTFMVrQz0px+up3SIHExnT7bs/ZajPjGbVHA8SOXI=;
	h=From:To:Subject:Date:From;
	b=CDcqPiTrEcKVzWXbztMcE0vXdx9hEl8HQ+Dez8mJ5u2gIjYEeVNYO+5NBu4f6DRGa
	 Sl5jyqYXI75Jyaia6Jk27Vx/552pfLAMutDLkUsVSECriZusH8OJ7ieCtK0hcz2dd3
	 +0KBV/hjYlXrHJ3oVqILGUf3nXXv4RsV4PFkDV613g/H3YvsnwiHqFUtDjru9cI7hm
	 2oQSjTXmeCwiFJPmOcgNtHDaSBwKrbXmB0QS7iousPKHKiYnUx7gagduHkTCe67zV6
	 SXBQxLCkGDJhTZOwOC2L580wiZxnW6QS2BuI5EYS7v2b59M0YOXBJT8dRuWtbmnTk2
	 s4MDnirx/ZF0w==
Received: from kali-mail.lab (kali-mail.lab [192.168.100.10])
	by kali-mail.lab (Postfix) with ESMTP id 9DD5230008E
	for <enjo@mail-server.lab>; Mon, 12 Jan 2026 13:28:39 -0500 (EST)
From: kali@kali-mail.lab
To: enjo@mail-server.lab
Subject: Sigurnosno upozorenje
Content-Type: text/plain; charset="utf-8"
Content-Transfer-Encoding: 8bit
MIME-Version: 1.0
Message-Id: <20260112182839.9DD5230008E@kali-mail.lab>
Date: Mon, 12 Jan 2026 13:28:39 -0500 (EST)

Vaš račun je zaključan.
Potvrdite identitet slanjem lozinke.
```

Korisnik kali je validan korisnik te se nije ništa promijenilo tijekom tranzita pa će SPF, DKIM i DMARC proći, makar je sam sadržaj poruke maliciozan.

## 2.4. Slanje poruke kada su podaci promijenjeni tijekom tranzita

Kod testiranja za promijene podataka mail poruke, prvo se mora isključiti openDKIM

```
sudo systemctl stop opendkim
```

Sada se može namjerno slomiti poruka. U skripti mail_custom_dkim.py se slamanje potpisa radi na slijedeći način:

```python
if dkim_cfg.get("break_signature"):
        signed = signed.replace(b"Subject:", b"Subject: BROKEN ", 1)
```

JSON payload izgleda ovako:  

```json
{
  "smtp": { "host": "kali-mail.lab", "port": 25 },

  "envelope": {
    "mail_from": "kali@kali-mail.lab",
    "rcpt_to": ["enjo@mail-server.lab"]
  },

  "headers": {
    "from": "kali@kali-mail.lab",
    "to": "enjo@mail-server.lab",
    "subject": "Tampered DKIM"
  },

  "body": {
    "text": "This message will be modified after signing"
  },

  "dkim": {
    "enabled": true,
    "domain": "kali-mail.lab",
    "selector": "default",
    "private_key": "keys/example_valid.pem",
    "break_signature": true
  }
}
```

Kao poruku, server prima:

```
Return-Path: <kali@kali-mail.lab>
X-Original-To: ubuntu@mail-server.lab
Delivered-To: ubuntu@mail-server.lab
Authentication-Results: OpenDMARC; dmarc=pass (p=quarantine dis=none) header.from=kali-mail.lab
Authentication-Results: mail-server.lab;
	dkim=fail reason="signature verification failed" (2048-bit key; unprotected) header.d=kali-mail.lab header.i=@kali-mail.lab header.a=rsa
-sha256 header.s=default header.b=AK1yvdxv;
	dkim-atps=neutral
Received: from kali-mail.lab (unknown [192.168.100.10])
	by mail-server.lab (Postfix) with ESMTPS id DE5E72A0378
	for <ubuntu@mail-server.lab>; Mon, 12 Jan 2026 18:18:01 +0000 (UTC)
Authentication-Results: OpenDMARC; dmarc=pass (p=quarantine dis=none) header.from=kali-mail.lab
Authentication-Results: OpenDMARC; spf=pass smtp.mailfrom=kali-mail.lab
Received: from kali-mail.lab (kali-mail.lab [192.168.100.10])
	by kali-mail.lab (Postfix) with ESMTP id D4DA0C0068
	for <ubuntu@mail-server.lab>; Mon, 12 Jan 2026 13:18:01 -0500 (EST)
DKIM-Signature: v=1; a=rsa-sha256; c=relaxed/simple; d=kali-mail.lab;
 i=@kali-mail.lab; q=dns/txt; s=default; t=1768241881; h=from : to :
 subject; bh=H4AJj2HQsyZMjF4IemfLEEtXPR4jqoRo4svfY1+KLA4=;
 b=AK1yvdxvzoeyiAziubYRSPkpHM2WS7DNHKXiiudJj12XzJHVbAe7aPn3KBL3bvDQqdUKh
 VEpdXms3VkqaUri+JTjnECc1mLyB7PtYwZV5HsgrZX8wjT5GQHtdPR7EF8ZBV0lOBHahMZu
 Ynm0B5zKvFAtJ5tzWGVLFNFJcWWejZe6jK1z6ITvnWmj036GJJy9Q5W+oslgFitLGcybtNI
 t+wZOd4JTNAdS8P3lkIpeLyuN16TBbpQh+N8qff7/NX40vWpL8EVeJ9MtLQll9SGO/rP0qZ
 sO0P13GLVbGppc2GMRNJr4FQX+isxzTo8K4Awpw2HPys6kFmCQbYuMdKlSRA==
From: kali@kali-mail.lab
To: ubuntu@mail-server.lab
Subject: BROKEN  Tampered DKIM
Content-Type: text/plain; charset="utf-8"
Content-Transfer-Encoding: 7bit
MIME-Version: 1.0
Message-Id: <20260112181801.D4DA0C0068@kali-mail.lab>
Date: Mon, 12 Jan 2026 13:18:01 -0500 (EST)

This message will be modified after signing
```

DKIM pada, ali SPF prolazi, budući da barem jedna od te dvije provjere prolazi, DMARC isto prolazi.

## 2.5. Slanje poruke bez DKIM potpisa
Ovdje korisnik pokušava poslati poruku bez da potpiše vlastitu poruku:

JSON payload izgleda ovako:

```json
{
  "smtp": { "host": "kali-mail.lab", "port": 25 },

  "envelope": {
    "mail_from": "kali@kali-mail.lab",
    "rcpt_to": ["enjo@mail-server.lab"]
  },

  "headers": {
    "from": "kali@kali-mail.lab",
    "to": "enjo@mail-server.lab",
    "subject": "Missing DKIM signature"
  },

  "body": {
    "text": "This message isn't signed"
  },

  "dkim": {
    "enabled": false
  }
}
```
Poruka na serveru izgleda ovako:  

```
Return-Path: <kali@kali-mail.lab>
X-Original-To: ubuntu@mail-server.lab
Delivered-To: ubuntu@mail-server.lab
Authentication-Results: OpenDMARC; dmarc=pass (p=quarantine dis=none) header.from=kali-mail.lab
Received: from kali-mail.lab (unknown [192.168.100.10])
	by mail-server.lab (Postfix) with ESMTPS id 8425A2A0378
	for <ubuntu@mail-server.lab>; Mon, 12 Jan 2026 18:17:57 +0000 (UTC)
Authentication-Results: OpenDMARC; dmarc=pass (p=quarantine dis=none) header.from=kali-mail.lab
Authentication-Results: OpenDMARC; spf=pass smtp.mailfrom=kali-mail.lab
Received: from kali-mail.lab (kali-mail.lab [192.168.100.10])
	by kali-mail.lab (Postfix) with ESMTP id 7ABA2C0068
	for <ubuntu@mail-server.lab>; Mon, 12 Jan 2026 13:17:57 -0500 (EST)
From: kali@kali-mail.lab
To: ubuntu@mail-server.lab
Subject: Missing DKIM signature
Content-Type: text/plain; charset="utf-8"
Content-Transfer-Encoding: 7bit
MIME-Version: 1.0
Message-Id: <20260112181757.7ABA2C0068@kali-mail.lab>
Date: Mon, 12 Jan 2026 13:17:57 -0500 (EST)

This message isn't signed
```

U ovoj slučaju, DKIM ne pada, ali, budući da DKIM potpisa ni nema, smatra se da je DKIM nevažeći. SPF prolazi, budući da je mail od validne osobe te time i DMARC prolazi.

## 2.6. Slanje poruke s nevažećim ključem
Ovdje se poruka potpisuje s nevažećim ključem, odnosno privatni ključ nije u paru s javnim ključem.  

JSON payload izgleda ovako:

```json
{
  "smtp": { "host": "kali-mail.lab", "port": 25 },

  "envelope": {
    "mail_from": "kali@kali-mail.lab",
    "rcpt_to": ["enjo@mail-server.lab"]
  },

  "headers": {
    "from": "kali@kali-mail.lab",
    "to": "enjo@mail-server.lab",
    "subject": "Invalid DKIM key"
  },

  "body": {
    "text": "This message is signed with an invalid key"
  },

  "dkim": {
    "enabled": true,
    "domain": "kali-mail.lab",
    "selector": "default",
    "private_key": "keys/example_invalid.pem",
    "break_signature": false
  }
}
```

Server na kraju dobije sljedeću poruku:  

```
Return-Path: <kali@kali-mail.lab>
X-Original-To: ubuntu@mail-server.lab
Delivered-To: ubuntu@mail-server.lab
Authentication-Results: OpenDMARC; dmarc=pass (p=quarantine dis=none) header.from=kali-mail.lab
Authentication-Results: mail-server.lab;
	dkim=fail reason="signature verification failed" (2048-bit key; unprotected) header.d=kali-mail.lab header.i=@kali-mail.lab header.a=rsa
-sha256 header.s=default header.b=yujHZr9Q;
	dkim-atps=neutral
Received: from kali-mail.lab (unknown [192.168.100.10])
	by mail-server.lab (Postfix) with ESMTPS id 7D7802A0378
	for <ubuntu@mail-server.lab>; Mon, 12 Jan 2026 18:17:52 +0000 (UTC)
Authentication-Results: OpenDMARC; dmarc=pass (p=quarantine dis=none) header.from=kali-mail.lab
Authentication-Results: OpenDMARC; spf=pass smtp.mailfrom=kali-mail.lab
Received: from kali-mail.lab (kali-mail.lab [192.168.100.10])
	by kali-mail.lab (Postfix) with ESMTP id 79F8CC0068
	for <ubuntu@mail-server.lab>; Mon, 12 Jan 2026 13:17:52 -0500 (EST)
DKIM-Signature: v=1; a=rsa-sha256; c=relaxed/simple; d=kali-mail.lab;
 i=@kali-mail.lab; q=dns/txt; s=default; t=1768241872; h=from : to :
 subject; bh=9NgScTTrLOULZQ//iLVR/oZK5A/7OtuGe/3LsP9rVZA=;
 b=yujHZr9QjRxE+4utTS7cO1tLuHwFVAXpzKWf+eAeB7sYXKA+42A/YupCNVnLkh1GawZF4
 5BIWaRcbhp4zH01UbjsNG8vaYXJi8m/5s68Vxg5xvESHtggGI+whygcZAUivcjYuTmQTNzh
 jBOh+XR9NonFzSUucfSfV76nBp6a4zgFQ6VULE67GxH9MU5MtzlBLR3nS0bEdySmZg3y52L
 pGMzF0Qnr/ohkbjxQBisYfgKesEi6c57RPjd6VlXbc0p822a+fKe8a6xsf0vnnWjKU5XhDB
 TNUGcrhX3OkRAwRGNXhrtkKjDvK+L1wWPrFekf2uzXZT7zPUT43FlP/0hGkw==
From: kali@kali-mail.lab
To: ubuntu@mail-server.lab
Subject: Invalid DKIM key
Content-Type: text/plain; charset="utf-8"
Content-Transfer-Encoding: 7bit
MIME-Version: 1.0
Message-Id: <20260112181752.79F8CC0068@kali-mail.lab>
Date: Mon, 12 Jan 2026 13:17:52 -0500 (EST)

This message is signed with an invalid key
```

Vidi se da DKIM opet pada, ali budući da je kali@kali-mail.lab validni mail, SPF i DMARC prolaze.
