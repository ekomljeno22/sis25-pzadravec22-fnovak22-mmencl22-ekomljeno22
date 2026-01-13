# Zaključak

Ovaj projekt bavi se sigurnošću elektroničke pošte kroz implementaciju DMARC protokola (_Domain-Based Message Authentication, Reporting & Conformance_).  Glavni cilj 
projekta bio je istražiti kako DMARC u kombinaciji sa SPF i DKIM protokolima može zaštititi domenu od neovlaštenog slanja e-pošte, odnosno spriječiti phishing i 
spoofing napade. Projekt je usmjeren na razumijevanje problema sigurnosti e-maila te na pokazivanje načina na koji se ti problemi mogu ublažiti pravilnom 
konfiguracijom sigurnosnih mehanizama.

U sklopu projekta implementirano je testno okruženje koje se sastoji od mail servera, DNS zapisa i alata za slanje i analizu mailova. Konfigurirani su SPF zapisi kako 
bi se odredili serveri koji su ovlašteni za slanje pošte, zatim DKIM za digitalno potpisivanje poruka kao te DMARC za definiranje pravila što učiniti s 
neautoriziranim porukama i prikupljanje izvještaja. Provedena su različita testiranja slanja mailova, neki su bili legitimni mailovi, a neki simulirani napadi kako bi 
se provjerilo kako sustav reagira u različitim situacijama. Analizom DMARC izvještaja i zapisa u logovima provjerila se učinkovitost implementiranih rješenja.

Rezultati projekta pokazuju da ispravna implementacija DMARC-a povećava razinu sigurnosti i smanjuje mogućnost zloupotrebe domene za slanje lažnih poruka. Sustav 
uspješno prepoznaje neovlaštene izvore i dobro primjenjuje definirane politike. Projekt potvrđuje važnost korištenja SPF-a, DKIM-a i DMARC-a kao temelja moderne 
sigurnosti e-maila.

Kao mogućnosti daljnjeg razvoja, projekt se može proširiti vizualizacije DMARC izvještaja za lakšu analizu podataka. Također je moguće provesti testiranja u 
složenijim i realnijim okruženjima s više domena i različitim mail serverima.

