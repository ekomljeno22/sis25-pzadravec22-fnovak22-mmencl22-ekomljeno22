# Plan

## 1. Planirani koraci u praktičnom dijelu
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

## 2. Planirani alati
- **Postfix**: Agent za slanje mail poruka.  
  Koristi se kao MTA (Mail Transfer Agent) koji upravlja isporukom i prosljeđivanjem e-mail poruka.  
  Omogućava slanje e-mailova s lokalnog poslužitelja i njihovu autentikaciju putem SPF i DKIM mehanizama.  
  Ključan je alat za testiranje DMARC konfiguracije i provjeru ispravnog slanja poruka.

- **Dovecot**: IMAP/POP3 server.  
  Omogućava pristup e-mail porukama putem IMAP ili POP3 protokola.  
  Koristi se za postavljanje i održavanje poštanskog sandučića u simuliranom okruženju.  
  Pruža podršku autentikaciji korisnika i sigurnom pristupu porukama.

- **OpenDKIM**: Implementacija DKIM protokola.  
  Omogućava digitalno potpisivanje e-mail poruka pomoću privatnog ključa i verifikaciju potpisa na strani primatelja.  
  Integrira se s Postfix-om kako bi osigurao autentikaciju pošiljatelja i spriječio lažiranje e-mail adresa.  
  Ključni alat u provedbi DMARC politike i zaštiti reputacije domene.

- **OpenDMARC**: Implementacija DMARC protokola.
  Omogućava provjeru DMARC pravila na temelju SPF i DKIM rezultata za dolazne e-mail poruke.
  Integrira se s Postfix-om kako bi se primijenile DMARC politike (none, quarantine, reject) definirane u DNS-u domene.
  Koristi se za generiranje i slanje DMARC izvještaja te za analizu usklađenosti poruka s definiranim sigurnosnim pravilima.

- **VirtualBox**: Stvaranje izoliranih virtualnih mašina za testiranje.  
  Omogućava postavljanje više virtualnih poslužitelja u zasebnim okruženjima.  
  Koristi se za testiranje različitih konfiguracija e-mail sustava bez rizika za stvarne servise.  
  Omogućava reprodukciju realnih mrežnih uvjeta i sigurnosnih scenarija.

- **Python**: Stvaranje skripti za simuliranje napada.  
  Koristi se za izradu automatiziranih testova i phishing simulacija.  
  Omogućava obradu i analizu DMARC izvještaja, kao i parsiranje XML datoteka.  
  Idealno za izgradnju prilagođenih alata koji podržavaju proces istraživanja i testiranja.

- **dmarcian**: Provjeravanje DMARC zapisa.  
  Online alat za validaciju i analizu DMARC, SPF i DKIM zapisa.  
  Omogućava vizualizaciju rezultata i otkrivanje pogrešaka u konfiguraciji.  
  Koristi se za praćenje učinka implementiranih sigurnosnih politika i optimizaciju DMARC postavki.




