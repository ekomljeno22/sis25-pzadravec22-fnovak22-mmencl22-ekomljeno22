# Implementacija DMARC-a (Domain-Based Message Authentication, Reporting & Conformance)

## **0. Struktura datoteka**

[TODO]

## **1. Pregled projekta**
Cilj projekta je detaljno razumjeti, implementirati i analizirati DMARC protokol. Studenti će simulirati organizacijsko okruženje, implementirati DMARC zajedno s SPF i DKIM, te procijeniti učinkovitost u smanjenju lažiranja (spoofing) i phishing napada.

## **2. Ciljevi**
- Razumjeti i implementirati DMARC te povezane protokole SPF i DKIM.
- Simulirati okruženje za slanje i primanje e-pošte.
- Analizirati učinkovitost DMARC-a u sprječavanju spoofing i phishing napada.
- Prikupiti i interpretirati DMARC izvještaje.
- Dokumentirati i prezentirati rezultate.

## **3. Struktura tima**
| Uloga                               | Opis                                                              | Član tima   |
| ----------------------------------- | ----------------------------------------------------------------- | ----------- |
| **DMARC Implementation Lead**       | Vodi implementaciju DMARC, SPF i DKIM.                            | Filip Novak |
| **Simulated Environment Lead**      | Postavlja i održava simulirano e-mail okruženje.                  | Marko Mencl  |
| **Attack and Reporting Lead**       | Dizajnira spoofing/phishing napade i upravlja DMARC izvještajima. | Ennio David Komljenović |
| **Analysis and Documentation Lead** | Analizira rezultate i izrađuje dokumentaciju.                     | Paula Zadravec |

## **4. Preduvjeti**
- Osnovno znanje e-mail protokola i DNS-a.
- Razumijevanje e-mail sigurnosti i napada (npr. spoofing, phishing).

## **5. Alati**
- **Postfix / Dovecot** – MTA i IMAP/POP3 server.
- **OpenDKIM** – DKIM implementacija.
- **VirtualBox / VMware** – Virtualizacija.
- **Python** – Skripte za simulaciju napada.
- **dmarcian** – Analiza i provjera DMARC zapisa i izvještaja.

## **6. Isporuke (Deliverables)**
- Konfigurirano email okruženje (DMARC, SPF, DKIM).
- Python skripte za napade.
- DMARC izvještaji prije i poslije optimizacije.
- Završni pisani izvještaj.
- Prezentacija (slajdovi).

## **7. Etička i pravna razmatranja**
- Svi napadi moraju biti izvedeni **isključivo** u izoliranom, virtualnom okruženju.
- Poštivanje **etičkih smjernica** i **zakonskih ograničenja** u svakom trenutku.
- Nikada ne koristiti stvarne domene ili produkcijske sustave bez dozvole.
