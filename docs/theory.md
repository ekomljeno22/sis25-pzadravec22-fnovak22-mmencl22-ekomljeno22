# Uvod
Napadači su posljednjih godina značajno unaprijedili svoje metode i koriste napredne tehnologije za izradu e-poruka koje izgledaju vrlo uvjerljivo što otežava razlikovanje legitimnih poruka od lažnih. Iako se većina phishing e-poruka može prepoznati, one koje ostanu neotkrivene predstavljaju ozbiljnu prijetnju i mogu ugroziti sigurnost. Napadač iskorištava ranjivosti SMTP kako bi pokrenuo napad lažiranja maila što je relativno jednostavno jer je taj protokol izvorno dizajniran bez ugrađenih sigurnosnih mehanizama. Pritom najčešće zloupotrebljavaju različita polja u zaglavljima e-maila. Napadači tako mogu kreirati uvjerljive lažne poruke koje se predstavljaju kao pouzdan izvor te tako uspješno provode phishing napade. Phishing se odnosi na pokušaj krađe osjetljivih podataka  putem lažnih poruka, a spoofing na lažiranje adrese pošiljatelja (Sethuraman i suradnici, 2024).

# SPF

SPF (Sender Policy Framework) je protokol namijenjen sprječavanju neželjenih mailova (spam poruke) i štiti domenu od phishing napada. Radi se o TXT zapisu unutar DNS postavki domene kojim se određuje koji su mail poslužitelji ovlašteni za slanje e-poruka u ime te domene (WMD Hosting, bez dat.).

SPF je transparentan i jednostavan za implementaciju jer koristi postojeću DNS infrastrukturu bez kriptografije. Slabosti uključuju ovisnost o DNSSEC-u protiv spoofinga i potrebu za ažuriranjem zapisa pri promjeni servera (Görling, 2007).

Kada mail server primi neki e-mail, provjerava SPF zapis domene s koje je poruka poslana. Ako IP adresa servera pošiljatelja nije navedena u SPF zapisu, poruka se može označiti kao neželjeni mail ili u potpunosti odbiti (WMD Hosting, bez dat.).

## SPF zapis i rezultati provjere

Primjer SPF zapisa:
```
v=spf1 ip4:123.0.122.8 -all
```
* to znači da samo IP 123.0.122.8 smije slati e-mail za ovu domenu
* v=spf1 označava SPF verziju
* -all znači da su svi ostali neovlašteni

Osnovni rezultati koje mail server može vratiti nakon usporedbe IP adrese pošiljatelja s onim u SPF zapisu su prema DuoCircle (bez dat.):
* **Pass** – IP adresa pošiljatelja ovlaštena je za slanje e-pošte s domene
* **Fail** – IP adresa pošiljatelja NIJE ovlaštena za slanje s domene
* **None** – domena nema taj SPF zapis


# DomainKeys Identified Mail (DKIM)
## Uvod
Prije uvođenja DKIM metode za verificiranje pošiljatelja, koristile su se razne metode kao crne liste gdje su poznati spam pošiljatelji bili zabranjeni slati poruke prema našim poslužiteljima i klijentima. Problem kod toga je bio da email protokoli nisu pregledavali je li email adresa lažirana (eng. spoofed), odnosno nismo mogli biti sigurni je li osoba koja je poslala tu poruku stvarno ta osoba.  

Jedna od mogućih metoda za provjeru pošiljatelja je DomainKeys Identified Mail, skraćeno DKIM. Metoda radi na jednostavnom principu digitalnog potpisa, gdje se u svaku poslanu poruku doda još jedno DKIM zaglavlje (Crocker, 2011; Leiba i Fenton, 2007)  

## DKIM potpis
Za stvaranje validnog DKIM potpisa, pošiljatelj mora prvo odlučiti koji će metapodaci biti spremljeni u zaglavlju. Od raznih metapodataka, sljedeći su obavezni:  
* v - verzija
* a - algoritam potpisivanja
* d - identifikator domene potpisivanja (eng. Signing domain identifier)
* s - selektor
* h - polja zaglavlja, polja koja su potpisana u poruci
* bh - hash tijela (eng. body hash)
* b - potpis zaglavlja i tijela
* t - vrijeme stvaranja (opcionalno, ali preporučeno)
* x - vrijeme isteka (opcionalno, ali preporučeno)
* c - algoritam kanonizacije, pretvaranje poruke u standardni oblik (opcionalno)
* q - metoda za traženje zapisa

Primjer zaglavlja:

```
DKIM-Signature: a=rsa-sha1; q=dns/txt; c=simple/simple;
d=example.com; s=appliances; i=@store.example.com;
t=1117574938; x=1118006938; h=from:to:subject:date;
bh=alIzndU2Nzg5jsEypzQ1njc4OTAxejr0NTY3ODkwdTI=;
b=dzdVyOfAKCdLXdJOc9G2q8LoXSlEniSbav+yuU4zGeeruD00lszZVoG4ZHRNiYzR
```

# Stvaranje i provjera hash vrijednosti
Prije stvaranja cijelog potpisa, mora se stvoriti par kriptografskih ključeva, jedan privatni, jedan javni. Privatni ključ ostaje kod pošiljatelja, a javni ključ se tipično sprema kao DNS zapis kod poslužitelja domene.  

Kako bi se mogla provjeriti autentičnost poruke, moraju se prvo stvoriti hash vrijednosti za h i bh metapodatke. Za bh (body hash) se jednostavno uzme sadržaj tijela poruke i napravi se hash vrijednost pomoću algoritma određenog pomoću metapodatka a. Metapodatak b se stvara tek kada su sva ostala zaglavlja i tijelo gotovi te se tada sve to stavlja u hash algoritam i hash vrijednost se zatim stavi kao vrijednost metapodatka b, nakon što se kriptira privatnim ključem pošiljatelja. Kada je zaglavlje gotovo, poruka se može poslati (Leiba i Fenton, 2007).

Zatim se na razini domene (ili izravno kod primatelja) provjerava validnost poruke. U zaglavlju DKIM potpisa se uzme selektor koji govori kako se zove identifikator javnog ključa, taj se ključ uzme iz mjesta gdje je pohranjen (tipično DNS server) pomoću tog selektora te se zatim dekriptira b. Ako se podaci podudaraju, odnosno je li dekriptirani hash validan, poruka se pošalje primatelju kao normalno, a ako se ne podudaraju (npr. dogodila se neka greška ili je pošiljatelj lažiran), posebni sustav onda odlučuje što će napraviti s porukom (Leiba i Fenton, 2007).

## Prednosti i nedostaci
DKIM kao metoda je odlična za implementaciju raznih sustava za sprječavanje spam i phishing poruka budući da osigurava integritet poruke (ako se bilo koji dio poruke promijeni, validacija odmah pada).  
Nažalost, problem kod DKIM metode je da ne može provjeriti što poruka sadrži, samo provjerava potpise. Ako je neka zloćudna osoba ukrala email adresu nekome, DKIM ne može provjeriti takav slučaj te ta osoba može slati bilo kakav sadržaj u porukama, gotovo uvijek maliciozan.  

Zato se uz DKIM još implementiraju i DMARC i SPF metode za potpunu osiguranost od napadača.


# DMARC

## Svrha i funkcija DMARC-a
DMARC (Domain-Based Message Authentication, Reporting & Conformance) je sigurnosni protokol koji pomaže organizacijama da zaštite svoje e-mail domene od lažiranja (spoofing) i phishing napada. Nadopunjuje SMTP (Simple Mail Transfer Protocol), osnovni protokol za slanje e-poruka, koji sam po sebi nema ugrađene mehanizme za provjeru autentičnosti pošiljatelja. SPF i DKIM se već godinama koriste za provjeru pošiljatelja e-maila, ali nisu omogućavali jasno definiranje što učiniti kada provjera ne uspije. Zbog toga vlasnici domena nisu imali potpunu kontrolu nad korištenjem svoje domene i zaštitom brenda i to je onda dovelo do potrebe za DMARC protokola (Fortinet, bez dat.).

DMARC koristi rezultate SPF i DKIM provjera kako bi potvrdio autentičnost e-maila, ako barem jedan uspije, e-mail se smatra legitimnim. DMARC zapis u DNS-u određuje pravila i prima XML izvještaje koji pokazuju tko sve šalje e-mailove u ime domene, uključujući i nepoznate ili neovlaštene izvore te pokušaje zloupotrebe (dmarcian, bez dat.). Ljudima ih je teško čitati i razumjeti, pogotovo kad ih može biti na tisuće (dmarcian, bez dat.).

## DMARC politike i izvještaji
Vlasnik domene postavlja politiku koja određuje što napraviti s porukama koje ne prođu provjeru. DMARC ima tri razine politike:
* **p=none** – služi za nadzor i ne utječe na isporuku e-maila, ovdje se samo prikupljaju informacije o DMARC provjerama koje će poslužitelj slati na adresu e-maila u DMARC zapisu
* **p=quarantine** – znači da se poruke koje ne prođu DMARC provjeru označavaju kao sumnjive, primjerice premještaju u spam folder
* **p=reject** – u potpunosti odbija poruke koje ne prolaze DMARC provjeru, odnosno takva se e-mail uopće ne prihvaća
(dmarcian, bez dat.).

DMARC se najčešće uvodi postupno. Počinje se s politikom p=none, koja omogućuje uvid u način korištenja domene te provjeru rada SPF-a i DKIM-a, a zatim se s vremenom prelazi na strožu politiku p=reject (dmarcian, bez dat.).

DMARC zapis se dodaje kao TXT zapis u DNS postavkama domene.
Osnovni DMARC zapis izgleda ovako:
```
**v=DMARC1; p=none; rua=mailto:vaš-email@domena.com**
```
* “v=” označava da je ovo DMARC zapis
* “p=” označava DMARC pravilo → p=none znači da se za sada samo prikupljaju izvještaji, bez blokiranja poruka
* rua je adresa na koju dolaze DMARC izvještaji, RUA izvještaji daju agregirani pregled ukupnog e-mail prometa određene domene
(dmarcian, 2020)

Primjer XML izvještaja:
```
<?xml version="1.0" encoding="UTF-8" ?>
<feedback>
  <report_metadata>
    <org_name>google.com</org_name>
    <email>noreply-dmarc-support@google.com</email>
    <extra_contact_info>https://support.google.com/a/answer/2466580</extra_contact_info>
    <report_id>4961312363692582822</report_id>
    <date_range>
      <begin>1477958400</begin>
      <end>1478044799</end>
    </date_range>
  </report_metadata>
  <policy_published>
    <domain>customer.com</domain>
    <adkim>s</adkim>
    <aspf>s</aspf>
    <p>reject</p>
  </policy_published>
</feedback>
```
(dmarcian, 2020)

Alignment znači usklađenost između adrese pošiljatelja koju vidi primatelj (u “From:” polju e-maila) i adrese koja se provjerava kroz SPF ili DKIM. Usklađivanje može biti da se samo provjerava osnovna domena i dopuštaju se različite poddomene, ili strogo gdje se mora točno podudarati cijela domena (Forinet, bez dat.).

## Značaj DMARC-a
E-mail je uključen u više od 90% svih mrežnih napada i bez DMARC-a može biti teško utvrditi je li e-mail stvaran ili lažan (dmarcian, bez dat.).
DMARC je najbolje implementirati na razini cijele organizacije, umjesto da se ograniči na pojedine domene.  Kako bi se spriječili prekidi u slanju poruka, važno je znati tko koristi domene u organizaciji i tko ima odgovornost nad trećim stranama (dmarcian, bez dat.).

Također, treba napomenuti kako je DMARC najučinkovitiji kad je politika postavljena na reject, ali to ujedno i rizik jer može dovesti do gubitka važnih, legitimnih poruka ako nisu svi sustavi ispravno konfigurirani.

Zahvaljujući DMARC-u, administratori e-pošte dobivaju veću kontrolu i sigurnost jer mogu biti sigurni da se s potencijalno opasnom ili lažnom poštom postupa u skladu s jasno definiranim pravilima (Loshin, 2024).

# Zajedničko djelovanje SPF-a, DKIM-a i DMARC-a

SPF, DKIM i DMARC čine zajedno osnovu zaštite kod e-maila. U nastavku slijedi način na koji oni surađuju kako bi spriječili phishing i spoofing napade:

* **SPF** predstavlja osnovu sustava za autentifikaciju e-maila. Njegova uloga je potvrditi da je domena s koje se poruka šalje zaista ovlaštena za slanje e-mailova. Zato je SPF nužan za ispravno korištenje DKIM-a i DMARC-a jer omogućuje provjeru tko ima pravo slati poruke u ime određene domene. SPF radi putem DNS zapisa koji sadrže popis mail servera ovlaštenih za slanje poruka. Ti se podaci razmjenjuju između servera prilikom dostave e-maila kako bi se potvrdio identitet pošiljatelja. SPF ne donosi odluku o tome što učiniti s porukom niti može utvrditi je li sadržaj poruke lažan, on samo potvrđuje je li poslužitelj ovlašten.

Dalje ulogu preuzimaju **DKIM i DMARC**.

* Kod **DKIM-a**, poruke koje šalju odgovarajući mail serveri digitalno su potpisane. Taj se potpis provjerava pomoću javnog ključa koji je zapisan u DNS-u domene pošiljatelja kroz DKIM zapis. Na taj se način potvrđuje da poruka nije izmijenjena tijekom prijenosa i da je stvarno poslana s navedene domene.

* **DMARC** se oslanja i na SPF i na DKIM kako bi definirao pravila za obradu e-maila. Putem DMARC zapisa u DNS-u vlasnik domene određuje kako bi primateljski mail poslužitelji trebali postupati s porukama koje ne prođu autentifikaciju, npr. hoće li ih odbiti, označiti kao SPAM ili samo nadzirati njihovu isporuku.

Kombinacijom ova 3 mehanizma, mail serveri mogu:
* provjeriti je li pošiljatelj ovlašten za slanje e-pošte s određene domene pomoću SPF-a,
* potvrditi autentičnost poruke provjerom DKIM digitalnog potpisa,
* primijeniti definirana pravila za sumnjive poruke koristeći DMARC


# Reference
Crocker, D., Hansen, T., i Kucherawy, M. (Eds.). (2011). DomainKeys Identified Mail (DKIM) signatures (RFC 6376). Internet Engineering Task Force. https://www.rfc-editor.org/rfc/rfc6376 (DOI: https://doi.org/10.17487/RFC6376)

dmarcian. (bez dat.). Getting started with DMARC. dmarcian. https://dmarcian.com/getting-started-with-dmarc/

dmarcian. (2020). What is a DMARC record? dmarcian. https://dmarcian.com/what-is-a-dmarc-record/ 

dmarcian. (bez dat.). Why DMARC? dmarcian. https://dmarcian.com/why-dmarc/

DuoCircle. (bez dat.). SPF neutral and other types of SPF error messages you could encounter after setting SPF records for your domain. DuoCircle. https://www.duocircle.com/content/spf-permerror/spf-neutral 

Fortinet. (bez dat.). DMARC. Fortinet. https://www.fortinet.com/resources/cyberglossary/dmarc 

Görling, S. (2007). An overview of the Sender Policy Framework (SPF) as an anti-phising mechanism. Internet Research, 17(2), 169–179. https://doi.org/10.1108/10662240710737022

Leiba, B., i Fenton, J. (2007). DomainKeys Identified Mail (DKIM): Using digital signatures for domain verification. CEAS 2007. https://www.researchgate.net/publication/221650803_DomainKeys_Identified_Mail_DKIM_Using_Digital_Signatures_for_Domain_Verification

Loshin, P. (2024). Email authentication: How SPF, DKIM and DMARC work together. TechTarget. https://www.techtarget.com/searchsecurity/answer/Email-authentication-How-SPF-DKIM-and-DMARC-work-together

Sethuraman, S. C., Devi Priya, V. S., Reddi, T., Mulka Sai Tharun Reddy, R., i Khan, M. K. (2024). A comprehensive examination of email spoofing: Issues and prospects for email security. Computers & Security, 137, 103600. https://doi.org/10.1016/j.cose.2023.103600

WMD Hosting. (n.d.). Što je SPF zapis? WMD Hosting. https://wmd.hr/upute/%C5%A1to-je-spf-zapis
