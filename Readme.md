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

## **6. Koraci projekta**

### **Korak 1: Postavljanje okruženja**
- Kreiranje virtualnih strojeva.
- Instalacija i konfiguracija mail servera (Postfix, Dovecot).

### **Korak 2: Implementacija SPF, DKIM i DMARC**
- Dodavanje DNS zapisa.
- Testiranje ispravnosti konfiguracije.

### **Korak 3: Simulacija komunikacije**
- Slanje legitimnih e-mailova.
- Praćenje ponašanja sustava.

### **Korak 4: Simulacija napada**
- Python skripte za spoofing i phishing.
- Generiranje lažnih poruka.

### **Korak 5: Analiza DMARC izvještaja**
**Aktivnost:** Analizirati izvještaje i procijeniti učinkovitost.  
**Zadaci:**
- Prikupiti DMARC izvještaje iz simuliranog okruženja.
- Koristiti dmarcian ili slične alate za interpretaciju.

### **Korak 6: Optimizacija i kalibracija**
**Aktivnost:** Poboljšati konfiguraciju.  
**Zadaci:**
- Prilagoditi DMARC, SPF i DKIM postavke na temelju rezultata.
- Ponovno pokrenuti napade i usporediti učinkovitost.

### **Korak 7: Dokumentacija i završno izvješće**
**Aktivnost:** Izraditi detaljan izvještaj.  
**Zadaci:**
- Dokumentirati svaki korak implementacije.
- Opisati napade, rezultate i optimizacije.
- Analizirati učinkovitost DMARC-a.

### **Korak 8: Prezentacija i dijeljenje znanja**
**Aktivnost:** Prezentirati rezultate.  
**Zadaci:**
- Izraditi prezentaciju (slajdovi).
- Prezentirati metodologiju i nalaze.
- Sudjelovati u Q&A i prikupiti feedback.

## **7. Isporuke (Deliverables)**
- Konfigurirano email okruženje (DMARC, SPF, DKIM).
- Python skripte za napade.
- DMARC izvještaji prije i poslije optimizacije.
- Završni pisani izvještaj.
- Prezentacija (slajdovi).

## **8. Etička i pravna razmatranja**
- Svi napadi moraju biti izvedeni **isključivo** u izoliranom, virtualnom okruženju.
- Poštivanje **etičkih smjernica** i **zakonskih ograničenja** u svakom trenutku.
- Nikada ne koristiti stvarne domene ili produkcijske sustave bez dozvole.
