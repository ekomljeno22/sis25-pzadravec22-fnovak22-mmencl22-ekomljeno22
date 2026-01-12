# Implementacija DMARC-a (Domain-Based Message Authentication, Reporting & Conformance)

**Članovi tima**
- Ennio David Komljenović
- Marko Mencl
- Filip Novak
- Paula Zadravec

## **1. Pregled projekta**
Cilj projekta je detaljno razumjeti, implementirati i analizirati DMARC protokol. Studenti će simulirati organizacijsko okruženje, implementirati DMARC zajedno s SPF i DKIM, te procijeniti učinkovitost u smanjenju lažiranja (spoofing) i phishing napada.

**Struktura datoteka**

- [docs](https://github.com/ekomljeno22/sis25-pzadravec22-fnovak22-mmencl22-ekomljeno22/tree/main/docs) - plan, teorija, zaključak, reference
- [implementation](https://github.com/ekomljeno22/sis25-pzadravec22-fnovak22-mmencl22-ekomljeno22/tree/main/implementation) - datoteke rezultate praktičnog dijela
- [presentation](https://github.com/ekomljeno22/sis25-pzadravec22-fnovak22-mmencl22-ekomljeno22/tree/main/presentation) - poveznica na prezentaciju
- [results](https://github.com/ekomljeno22/sis25-pzadravec22-fnovak22-mmencl22-ekomljeno22/tree/main/results) - neki screenshotovi i logovi

## **2. Ciljevi**
- Razumjeti i implementirati DMARC te povezane protokole SPF i DKIM.
- Simulirati okruženje za slanje i primanje e-pošte.
- Analizirati učinkovitost DMARC-a u sprječavanju spoofing i phishing napada.
- Prikupiti i interpretirati DMARC izvještaje.
- Dokumentirati i prezentirati rezultate.

Zadaci:
- Implementacija i konfiguracija DMARC, SPF i DKIM zapisa
- Postavljanje i održavanje simuliranog e-mail okruženja
- Dizajniranje spoofing i phishing napada te upravljanje DMARC izvještajima
- Analiza dobivenih rezultata i izrada dokumentacije


## **3. Preduvjeti**
- Osnovno znanje e-mail protokola i DNS-a.
- Razumijevanje e-mail sigurnosti i napada (npr. spoofing, phishing).

## **4. Alati**
- **Postfix / Dovecot** – MTA i IMAP/POP3 server.
- **OpenDKIM** – DKIM implementacija.
- **VirtualBox / VMware** – Virtualizacija.
- **Python** – Skripte za simulaciju napada.
- **dmarcian** – Analiza i provjera DMARC zapisa i izvještaja.

## **5. Isporuke (Deliverables)**
- Konfigurirano email okruženje (DMARC, SPF, DKIM).
- Python skripte za napade.
- DMARC izvještaji prije i poslije optimizacije.
- Završni pisani izvještaj.
- Prezentacija (slajdovi).

## **6. Etička i pravna razmatranja**
- Svi napadi moraju biti izvedeni **isključivo** u izoliranom, virtualnom okruženju.
- Poštivanje **etičkih smjernica** i **zakonskih ograničenja** u svakom trenutku.
- Nikada ne koristiti stvarne domene ili produkcijske sustave bez dozvole.
