# Plan

## Planirani alati
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



