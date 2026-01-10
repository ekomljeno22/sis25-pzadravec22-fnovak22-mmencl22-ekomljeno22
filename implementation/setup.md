## 1. Postavljanje virtualne okoline

### 1.1 Preuzimanje programa i datoteka

Prvo je potrebno preuzeti i instalirati program Oracle Virtual Box na poveznici: https://www.virtualbox.org/wiki/Downloads .
Za ovaj projekt, koristila se verzija Windows hosts (v 7.2.4).

Zatim je potrebno preuzeti datoteke za virtualne strojeve. Koristit će se dva virtualna stroja: jedan Kali Linux, a drugi običan Ubuntu.


Kali Linux virtualni stroj se preuzima na slijedećoj poveznici: https://www.kali.org/get-kali/#kali-virtual-machines . Potrebno je odabrati vrstu virtualnog stroja koja je prikladna za Oracle VirtualBox (vidi sliku ispod).

<p align="center">
 <a href="https://github.com/user-attachments/assets/ef2e2c4b-264d-4cfd-bd50-b9c067b72dff?raw=true" target="_blank">
  <img src="https://github.com/user-attachments/assets/ef2e2c4b-264d-4cfd-bd50-b9c067b72dff" width="700"/>
  <a/>
<p/>

U trenutnu izrade projekta, koristila se slijedeća verzija Kali Linux vritualnog stroja: `kali-linux-2025.3-virtualbox-amd64` .


Ubuntu virtualni stroj se preuzima na slijedećoj poveznici (vidi sliku ispod): https://ubuntu.com/download/desktop.

<p align="center">
 <a href="https://github.com/user-attachments/assets/b911d4a7-cea1-4333-a96c-ce1484ce06b2?raw=true" target="_blank">
  <img src="https://github.com/user-attachments/assets/b911d4a7-cea1-4333-a96c-ce1484ce06b2" width="700"/>
  <a/>
<p/>

U trenutnu izrade projekta, koristila se slijedeća verzija Ubuntu vritualnog stroja: `ubuntu-24.04.3-desktop-amd64.iso` .

Virtualni stroj Ubuntu će biti Mail server, a virtual stroj Kali Linux će biti napadač na Mail server.


### 1.2 Postavljanje virtualnih strojeva unutar VirtualBox-a

**Kali Linux**

Prvo je potrebno raspakirati preuzetu zip arhivu.
Nakon raspakiravanja bi se trebale pojaviti dvije datoteke: `.vbox` i `.vdi`.
Ako je moguće, preporuča se pohraniti datoteke na SDD disk radi boljih performansa.
Kako bi se virtualni stroj ubacila u VirtualBox, potrebno je napraviti dvostruki klik na `.vbox` datoteku.
Ako je sve dobro, virtualni stroj bi se trebao pojaviti u listi virtualnih strojeva (vidi sliku ispod):

<p align="center">
 <a href="https://github.com/user-attachments/assets/51fbb6ea-671f-4d8e-89ea-7632fde565f8?raw=true" target="_blank">
  <img src="https://github.com/user-attachments/assets/51fbb6ea-671f-4d8e-89ea-7632fde565f8" width="300"/>
  <a/>
<p/>

**Ubuntu**

Prvo je potrebno pokrenuti program VirtualBox. Zatim u glavnom izborniku treba odabrati "Machines" i nakon toga pritisnuti gumb "New".
Otvara se čarobnjak za postavljanje novog virtualnog stroja. 

1. Grupa opcija: "Virtual machine name and operating system".

Potrebno dodijeliti ime virtualnom stroju, odabrati mjesto gdje će se pohraniti njegove datoteke, i najvažnije, potrebno je odabrati ispravnu datoteku instalacije virtualnog stroja Ubnutnu (vidi sliku ispod).

<p align="center">
 <a href="https://github.com/user-attachments/assets/830f036a-1a9b-44c6-9f5e-13521a6b8901?raw=true" target="_blank">
  <img src="https://github.com/user-attachments/assets/830f036a-1a9b-44c6-9f5e-13521a6b8901" width="700"/>
  <a/>
<p/>


2. Grupa opcija: "Set up unattended guest OS installation"

Ovdje je potrebno dodijeliti vlastito proizvoljno korisničko ime i lozinku (lozinku je potrebno zapamtiti jer će biti potrebna za pristup).
Host name i domain name za sada nije toliko bitan jer se oni mogu kasnije mijenjati po potrebi.
OBAVEZNO odabrati opciju "Install Guest Additions" kako bi virtualni stroj mogao imati bolje performanse.

<p align="center">
 <a href="https://github.com/user-attachments/assets/efc960bc-e4af-4e14-a8de-3d84a3909cdd?raw=true" target="_blank">
  <img src="https://github.com/user-attachments/assets/efc960bc-e4af-4e14-a8de-3d84a3909cdd" width="700"/>
  <a/>
<p/>

3. Grupa opcija: "Specify virtual hardware"

Preporuča se dodijeliti najmanje 4GB rama i barem dva procesora. Također se preporuča ostati u zelenom području kod oba klizača.


<p align="center">
 <a href="https://github.com/user-attachments/assets/3ac5df0b-b67c-4ba0-9da2-c05c41296383?raw=true" target="_blank">
  <img src="https://github.com/user-attachments/assets/3ac5df0b-b67c-4ba0-9da2-c05c41296383" width="700"/>
  <a/>
<p/>

4. Grupa opcija: "Specify virtual hard disk"

Potrebno je stvoriti novi virtualni hard disk. Preporuča se uzeti batem 30GB prostora.

<p align="center">
 <a href="https://github.com/user-attachments/assets/88bf1540-0696-43e5-a738-3cd364c7c6bd?raw=true" target="_blank">
  <img src="https://github.com/user-attachments/assets/88bf1540-0696-43e5-a738-3cd364c7c6bd" width="700"/>
  <a/>
<p/>


Konačno, potrebno je pritisnuti gumb "Finish".
Nakon toga se automatski pokreće virtualni stroj i na njemu se pokreću dodatne instalacije.
Potrebno je ostaviti virtualni stroj da se do kraja instalira.
Ovo može potrajati i sat vremena, ovisno o brzini host računala.
Kada se u virtualnom stroju pojavi prozor za prijavu, tada je instalacija uspiješma.
(Napomena: Ukoliko piše da je nakon instalacije došlo do neke pogreške, samo je potrebno isključiti virtualni stroj i ponovo ga pokrenuti. Tada će instalacija biti dovršena. Ako se je moguće prijaviti u virtualnom stroju, tada je sve uredu.).

### 1.3 Konfiguriranje virtualnih strojeva unutar VirtualBox-a

Potrebno je izraditi novi NAT Network kako bi virtualni strojevi mogli imati pristup internetu.
Za to se mora otići na Network karticu u glavnom izborniku VirtualBox-a (ili File -> Tools -> Network).
Pod karticom "NAT Networks" je potrebno dodati novu NAT mrežu sa slijedećim postavkama (vidi sliku ispod):


<p align="center">
 <a href="https://github.com/user-attachments/assets/a3f89713-f868-460a-afd7-2d71163306ff?raw=true" target="_blank">
  <img src="https://github.com/user-attachments/assets/a3f89713-f868-460a-afd7-2d71163306ff" width="900"/>
  <a/>
<p/>


**Kali Linux**

U kartici za pregled dostupnih virtualnih strojeva je potrebno odabrati virtualni stroj Kali Linux i zatim pritisnuti gumb "Settings".
Preporuča se odmah pod karticom General, u Features odabrati "Bidirectional" za opcije "Shared clipboard" i "Drag-and-drop".
Zatim je potrebno otići na karticu Network.
Potrebno je postaviti dva mrežna adaptera.
Za Adapter 1 je potrebno postaviti:
 - ✅ Enable Network Adapter
 - Attached to: `NAT Network`
 - Name: `NatNetwork`

I za Adapter 2:
 - ✅ Enable Network Adapter
 - Attached to: `Internal Network`
 - Name: `intnet`


Zatim je potrebno spremiti promijene i pokrenuti virtualni stroj Kali Linux.
Zadane vrijednosti korisničkog imena i lozinke za Kali Linux su:
 - Korisničko ime: `kali`
 - Lozinka: `kali`

Nakon dolaska na radnu površinu, potrebno je otvoriti komandnu liniju (terminal).
To se može napraviti tako da se pritisne desni klik miša bilo gdje na radnoj površini i odabere se opcija "Open Terminal Here".
Potrebno je testirati ako radi veza s internetom na način da se upiše komanda `ping 1.1.1.1`.
Ako ping radi, tada preskočite slijedeće korake za popravljanje NAT mreže i nastavite na dijelu za postavljanje unutarnje mreže.

Ako ping ne radi tada se pojavi poruka `ping: connect: Network is unreachable`.
Najvjerojatnije je problem da u novijim verzijama VirtualBox-a i Windowsa, VirtualBox DHCP server ponekad pokvari.

Prvo je potrebno u komandnoj liniji upisati slijedeće komande ovim redoslijedom:
 - `sudo ip addr add 10.0.2.15/24 dev eth0`
 - `sudo ip route add default via 10.0.2.2`
 - `echo "nameserver 8.8.8.8" | sudo tee /etc/resolv.conf`

Sada bi bing trebao raditi jer smo ručno dodijelili IP adresu mrežnom sučelju za NAT. Ipak je potrebno da se ručno može dobiti IP adresa iz DHCP servera za NAT pa je još potrebno napraviti nekoliko koraka:

Unijeti u komandnoj liniji slijedeće komande ovim redoslijedom
 - `sudo apt update`
 - `sudo apt install isc-dhcp-client`


Potrebno je unijeti i slijedeću komandu kako se bi spremio kasnije dodani DNS:
- `sudo nmcli con mod "Wired connection 1" ipv4.ignore-auto-dns yes`

 - `sudo ip addr del 10.0.2.15/24 dev eth0`

Zatim ugasite i ponovo pokrenite virtualni stroj Kali Linux.
Nakon ponovog pokretanja, unesite komandu koja šalje DHCP zahtjev za dobivanje IP adrese:
 - `sudo dhclient -v eth0`

Sada bi naredba `ping 1.1.1.1` trebala ispravno raditi.

Sada je još potrebno postaviti unutarnju mrežu kako bi virtualni strojevi mogli međusobno komunicirati.
Virtualnim strojevima će se ručno dodijeliti IP adrese za unutarnju mrežu.

U postavkama Kali Linux-a, potrebno je ručno postaviti statičnu IP adresu s slijedećim parametrima:

<p align="center">
 <a href="https://github.com/user-attachments/assets/914a7ccf-473b-4fb6-a30e-d7876c4004e5?raw=true" target="_blank">
  <img src="https://github.com/user-attachments/assets/914a7ccf-473b-4fb6-a30e-d7876c4004e5" width="600"/>
  <a/>
<p/>

Potrebno je spremiti provjere i provjeriti ako je sve uredu.


Provjera IP adresa: `ip a`

<p align="center">
 <a href="https://github.com/user-attachments/assets/fb80ec80-fce4-40c3-a078-4cab58fedf34?raw=true" target="_blank">
  <img src="https://github.com/user-attachments/assets/fb80ec80-fce4-40c3-a078-4cab58fedf34" width="600"/>
  <a/>
<p/>


Ukoliko statična IP adresa nije vidljiva, potrebno je koristiti ovu naredbu:
 - `sudo ip addr add 192.168.100.10/24 dev eth1`

**Ubuntu**

U kartici za pregled dostupnih virtualnih strojeva je potrebno odabrati virtualni stroj Ubuntu i zatim pritisnuti gumb "Settings".
Preporuča se odmah pod karticom General, u Features odabrati "Bidirectional" za opcije "Shared clipboard" i "Drag-and-drop".
Zatim je potrebno otići na karticu Network.
Potrebno je postaviti dva mrežna adaptera.
Za Adapter 1 je potrebno postaviti:
 - ✅ Enable Network Adapter
 - Attached to: `NAT Network`
 - Name: `NatNetwork`

I za Adapter 2:
 - ✅ Enable Network Adapter
 - Attached to: `Internal Newtork`
 - Name: `intnet`


Zatim je potrebno spremiti promijene i pokrenuti virtualni stroj.
Za pristup virtualnom stroju, potrebno je unijeti vrijednosti korisničkog imena i lozinke koje su bile postavljene ranije kod stvaranja virtualnog stroja.

Nakon dolaska na radnu površinu, potrebno je otvoriti komandnu liniju (terminal).
To se može napraviti tako da se pritisne desni klik miša bilo gdje na radnoj površini i odabere se opcija "Open in Terminal".
Potrebno je testirati ako radi veza s internetom na način da se upiše komanda `ping 1.1.1.1`.
Ako ping radi, tada preskočite slijedeće korake za popravljanje NAT mreže i nastavite na dijelu za postavljanje unutarnje mreže.

Ako ping ne radi tada se pojavi poruka `ping: connect: Network is unreachable`.
Najvjerojatnije je problem da u novijim verzijama VirtualBox-a i Windowsa, VirtualBox DHCP server ponekad pokvari.

Prvo je potrebno u komandnoj liniji upisati slijedeće komande ovim redoslijedom:
- `sudo ip addr add 10.0.2.16/24 dev enp0s3`
- `sudo ip route add default via 10.0.2.2`
- `echo "nameserver 8.8.8.8" | sudo tee /etc/resolv.conf`

Sada bi bing trebao raditi jer smo ručno dodijelili IP adresu mrežnom sučelju za NAT. Ipak je potrebno da se ručno može dobiti IP adresa iz DHCP servera za NAT pa je još potrebno napraviti nekoliko koraka:

Unijeti u komandnoj liniji slijedeće komande ovim redoslijedom
 - `sudo apt update`
 - `sudo apt install isc-dhcp-client`
 - `sudo ip addr del 10.0.2.16/24 dev enp0s3`


Zatim ugasite i ponovo pokrenite virtualni stroj.
Nakon ponovog pokretanja, unesite komandu koja šalje DHCP zahtjev za dobivanje IP adrese:
 - `sudo systemctl restart NetworkManager`
 - `sudo dhclient -v enp0s3`


Sada bi naredba `ping 1.1.1.1` trebala ispravno raditi.

Sada je još potrebno postaviti unutarnju mrežu kako bi virtualni strojevi mogli međusobno komunicirati.
Virtualnim strojevima će se ručno dodijeliti IP adrese za unutarnju mrežu.
a to je potrebno otići u Ubuntu na postavke:
 - Ikonica Ubuntu dole lijevo -> Settings -> Network -> enp0s8 postavke -> IPv4
 - - IPv4 Method: Manual
 - - Adresses:
 - - - Adress: `192.168.100.50`
 - - - Netmask: `255.255.255.0`
 - - Pritisnuti Apply
 

**Testiranje povezanosti VM-ova putem unutarnje mreže**

Na Kali Linux je potrebno testirati ako ispravno radi naredba ping (trebala bi raditi ispravno):
 - `ping 192.168.100.50`



## 2. Postavljanje Mail servera

### 2.1 Ubuntu Mail server

#### 2.1.1 Postfix (SMTP server)

Postavite hostname:
- `sudo hostnamectl set-hostname mail-server.lab`

Urdite hostnames (statičku lokalnu DNS tablicu):
- `sudo nano /etc/hosts`
- Potrebno je dodati zapise: 
- - `192.168.100.50 mail-server.lab mail-server`

Postavljanjem hostname-a i lokalnog mapiranja u `/etc/hosts` osigurava se ispravan identitet mail servera unutar SMTP komunikacije. 
Ovo je preduvjet za pravilno funkcioniranje i analizu SPF, DKIM i DMARC mehanizama.

Instaliranje Postfix-a:
- `sudo apt update`
- `sudo apt install postfix -y`

Prilikom instalacije Postifix-a odabrati:
- Opcija: `Internet Site`
- System mail name: `mail-server.lab`

Provjera ako Postfix servis radi:
- `systemctl status postfix`
- Ponovo pokretanje (ponekad zatreba): 
- - `systemctl stop postfix`
- - `systemctl start postfix`


Instaliranje `mailutils`, za slanje test mailova:
- `sudo apt install mailutils -y`

Testiranje slanja mailova (lokalno, na jednom virtualnom stroju):

```
echo "Postfix radi" | mail -s "Test" root
sudo su -
mail
Unijeti broj: 1
```

Trebao bi se vidjeti poslani mail.
Za izlaz iz `mail` naderbe: `quit()`
Konačno, potrebno se je vratiti na početnog korisnika: `su - [korisnik]`


Ako se želi, može se isprobati rad s više korisnika:

```
sudo adduser bob
sudo adduser alice

su - alice
echo "Pozdrav Bob!" | mail -s "Test mail" bob

su - bob
mail
1
```

Mail server je funkcionalan u lokalnoj mreži. 
Testni korisnici Alice i Bob mogu međusobno razmjenjivati mailove.




#### 2.1.2 BIND9 (DNS server)

Potrebno je postaviti lokalni DNS server. Za to će se koristiti servis BIND9 (aka named).


Instalacija BIND9 (to je lokalni DNS)
- `sudo apt install bind9 -y`

Zatim je potrebno u mrežnim postavkama za oba mrežna sučelja postaviti da izričito koriste samo lokalni DNS server.

To se radi na način da se ode na:
 - Ubuntu ikonu (dole lijevo) -> Settings -> Network -> Ethernet (enp0s3) settings --> IPv4
   - Postaviti IPv4 Method na `Automatic (DHCP)`
   - Postaviti DNS servers na `192.168.100.50` i isključiti Automatic!
   - Apply
 - Kod Ethernet (enp0s8) je potrebno:
   - postaviti DNS server na `192.168.100.50`


Unijeti `sudo nmcli connection show`:
```
NAME            UUID                                  TYPE      DEVICE 
profile-enp0s3  99e2c783-24c7-4837-92f9-716e63340bec  ethernet  enp0s3 
profile-enp0s8  9e65b200-5a9a-4e4b-8671-b0e8a58ffb1e  ethernet  enp0s8 
lo              817195e6-6940-49ea-ac24-35a5ee93d68e  loopback  lo 
```

Potrebno je identificirati NAME za enp0s3. Kada se zna NAME, mora se isključiti auto-dns:
```
sudo nmcli connection modify "profile-enp0s3" ipv4.ignore-auto-dns yes
sudo systemctl restart NetworkManager
```

`sudo nano /etc/bind/named.conf.local`:

Mora izgledati ovako:
```
zone "mail-server.lab" {
    type master;
    file "/etc/bind/db.mail-server.lab";
};

zone "kali-mail.lab" {
    type forward;
    forwarders { 192.168.100.10; };
};
```

`sudo nano /etc/bind/named.conf.options`:

Mora izgledati ovako:
```
options {
        directory "/var/cache/bind";
        allow-query { 127.0.0.1; 192.168.100.0/24; };
        listen-on { 127.0.0.1; 192.168.100.50; };
        allow-recursion { 127.0.0.1; 192.168.100.0/24; };
        recursion yes;
        forwarders {
                1.1.1.1;
                8.8.8.8;
        };
        dnssec-validation no;
};

```

Na kraju je potrebno restartati BIND DNS server:
- `sudo systemctl restart bind9`

Ovdje će se dodavati DNS TXT zapisi za SPF, DKIM i DMARC.

#### 2.1.3 SPF

##### 2.1.3.1 Kreiranje SPF TXT zapisa


Uređivanje DNS zapisa:
- `sudo nano /etc/bind/db.mail-server.lab`

Ovdje se postavljaju DNS zapisi i dodaje se SPF TXT zapis:
```
;
; BIND data file for local loopback interface
;
$TTL	604800
@	IN	SOA	mail-server.lab. root.mail-server.lab. (
			      2		; Serial
			 604800		; Refresh
			  86400		; Retry
			2419200		; Expire
			 604800 )	; Negative Cache TTL
;
@	IN	NS	mail-server.lab.
@	IN	A	192.168.100.50
@	IN	TXT	"v=spf1 ip4:192.168.100.50 ~all"
```

Nakon promijene DNS zapisa, potrebno je ponovo pokrenuti BIND9 servis.
- `sudo systemctl restart bind9`


Testiranje:
`dig txt mail-server.lab`:
```
;; ANSWER SECTION:
mail-server.lab. 604800 IN TXT "v=spf1 ip4:192.168.100.50 ~all"
```


##### 2.1.3.2 Dodavanje SPF provjere dolaznim mailovima

Instalacije skripte za provjeru SPF-a:
- `sudo apt install postfix-policyd-spf-python`



Uređivanje Postfix servisa:

`sudo nano /etc/postfix/master.cf`

Na kraj je potrebno dodati:
```
policyd-spf unix - n n - 0 spawn user=policyd-spf argv=/usr/bin/policyd-spf
```


Uređivanje Postfix globalne konfiguracije:

 `sudo nano /etc/postfix/main.cf`

Potrebno je dodati na kraj:
```
policyd-spf_time_limit = 3600
smtpd_recipient_restrictions =
   permit_mynetworks,
   permit_sasl_authenticated,
   reject_unauth_destination,
   check_policy_service unix:private/policyd-spf
```

Zatim je potrebno ponovo pokrenuti Postfix servis kako bi se primijenile promijene:
- `sudo systemctl stop postfix`
- `sudo systemctl start postfix`

Sada će se u dolaznim mailovima raditi SPF provjera.


#### 2.1.4 DKIM
##### 2.1.4.1  DKIM instalacija i konfiguracija

Instalacija alata za DKIM:
- `sudo apt install opendkim opendkim-tools -y`

Dodaje korisnika postfix u grupu opendkim (potrebno zas ispravni rad):
- `sudo gpasswd -a postfix opendkim`


Konfiguriranje OpenDKIM-a:
`sudo nano /etc/opendkim.conf`:

Potrebno je odkomentirati Logwhy i postaviti na yes:
```
Logwhy yes
```

Ovaj dio urediti da izgleda ovako:
```
Canonicalization        relaxed/simple
Mode                    sv
SubDomains              no
```

Ispod SubDomains je potrebno dodati:
```
AutoRestart         yes
AutoRestartRate     10/1M
Background          yes
DNSTimeout          5
SignatureAlgorithm  rsa-sha256
```

Na kraju je još potrebno ovdje dodati:
```
Nameservers             127.0.0.1
```

Ne smije se dva puta pojavljivati zapis Nameservers, stoga je potrebno zakomentirati sve ostale Nameservers zapise...

I zakomentirati `TrustAnchorFile`:
```
#TrustAnchorFile                /usr/share/dns/root.key
```

Na čisti kraj dodati:

```
# Map domains in From addresses to keys used to sign messages
KeyTable           refile:/etc/opendkim/key.table
SigningTable       refile:/etc/opendkim/signing.table

# Hosts to ignore when verifying signatures
ExternalIgnoreList  /etc/opendkim/trusted.hosts

# A set of internal hosts whose mail should be signed
InternalHosts       /etc/opendkim/trusted.hosts
```


##### 2.1.4.2  DKIM ključevi

Sada je potrebno kreirati ključeve i tablice:
```
sudo mkdir /etc/opendkim
sudo mkdir /etc/opendkim/keys
sudo chown -R opendkim:opendkim /etc/opendkim
sudo chmod go-rw /etc/opendkim/keys
```


`sudo nano /etc/opendkim/signing.table`:
```
*@mail-server.lab default._domainkey.mail-server.lab
*@*.mail-server.lab default._domainkey.mail-server.lab
```


`sudo nano /etc/opendkim/key.table`:
```
default._domainkey.mail-server.lab mail-server.lab:default:/etc/opendkim/keys/mail-server.lab/default.private
```

`sudo nano /etc/opendkim/trusted.hosts`:
```
127.0.0.1
::1
localhost
.mail-server.lab
192.168.100.50
```


Kreiranje javnog i privatnog ključa:

```
sudo mkdir /etc/opendkim/keys/mail-server.lab
sudo opendkim-genkey -b 2048 -d mail-server.lab -D /etc/opendkim/keys/mail-server.lab -s default -v
sudo chown opendkim:opendkim /etc/opendkim/keys/mail-server.lab/default.private
sudo chmod 600 /etc/opendkim/keys/mail-server.lab/default.private
```

Objavljivanje javnog ključa:
- `sudo cat /etc/opendkim/keys/mail-server.lab/default.txt`

Iskopirati ovaj dio:
```
default._domainkey	IN	TXT	( 
 "v=DKIM1; h=sha256; k=rsa; "
 "p=MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEApx4K4yOYuMdpeYv3YQf2MoocCADgXCpHyIyzsGzNFdH5ZmnV+zPywvR8UjLZ6TzW6bjth8WIMHVVTB2akbrypfez7q+QGjxh6UNiJWMFUXf5Jl113gl06IM68IWgd//LG6PWQH9b0Nv5zqVeEakiRaYVQei4MvpAXp0cJw5qbRiCFk7DmJha0L39alFYUdM5GG4amephGVcXEE"
 "cxd9/URJM0hEcTNX+HOk/p0F8uDoCZcThul5PJFKvFXk28ishvBbrRDAJWRmgCnryq5Vbo/8U7+HbbUSgGBmekywBIGY76F3Je+KybBGAvF2eI+Zh/SLbN7TaEVfXf9Py6KPLDhwIDAQAB"
)
```

Sada je potrebno urediti DNS zapise u BIND9:
`sudo nano /etc/bind/db.mail-server.lab`:

Treba ovako izgledati (Serial povećati za 1, ukloniti razmake u vrijednosti DKIM TXT + razdvojiti stringove jer je max 255 znaka po stringu, sve u jednoj liniji OBAVEZNO):
```
;
; BIND data file for local loopback interface
;
$TTL    604800
@       IN      SOA     mail-server.lab. root.mail-server.lab. (
                              3         ; Serial
                         604800         ; Refresh
                          86400         ; Retry
                        2419200         ; Expire
                         604800 )       ; Negative Cache TTL
;
@       IN      NS      mail-server.lab.
@       IN      A       192.168.100.50
@       IN      TXT     "v=spf1 ip4:192.168.100.50 ~all"

default._domainkey IN TXT ("v=DKIM1;h=sha256;k=rsa;" "p=MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEApx4K4yOYuMdpeYv3YQf2MoocCADgXCpHyIyzsGzNFdH5ZmnV+zPywvR8UjLZ6TzW6bjth8WIMHVVTB2akbrypfez7q+" "QGjxh6UNiJWMFUXf5Jl113gl06IM68IWgd//LG6PWQH9b0Nv5zqVeEakiRaYVQei4MvpAXp0cJw5qbRiCFk7DmJha0L39alFYUdM5GG4amephGVcXEE" "cxd9/URJM0hEcTNX+HOk/p0F8uDoCZcThul5PJFKvFXk28ishvBbrRDAJWRmgCnryq5Vbo/8U7+HbbUSgGBmekywBIGY76F3Je+KybBGAvF2eI+Zh/SLbN7TaEVfXf9Py6KPLDhwIDAQAB")

```

Zatim: `sudo systemctl restart bind9`.


Potrebno je ponovo pokrenuti opendkim servis:
- `sudo systemctl restart opendkim`


Testiranje opendkim ključeva:
-`sudo opendkim-testkey -d mail-server.lab -s default -vvv`
- U ispisu bi se trebalo na kraju vidjeti `key OK`



##### 2.1.4.3 Spajanje Postfix sa OpenDKIM

Stvoriti direktorij u kojem će se postaviti Socket za komunikaciju Postfix <-> OpenDKIM:
```
sudo mkdir /var/spool/postfix/opendkim
sudo chown opendkim:postfix /var/spool/postfix/opendkim
```

Uređivanje konfiguracije OpenDKIM-a:
`sudo nano /etc/opendkim.conf`

Dio sa socketima mora se promijniti u ovo:
```
#Socket			local:/run/opendkim/opendkim.sock
#Socket			inet:8891@localhost
#Socket			inet:8891
Socket			local:/var/spool/postfix/opendkim/opendkim.sock
```


`sudo nano /etc/default/opendkim`
Zakomentirati stari SOCKET i staviti novi:
```
#SOCKET=local:$RUNDIR/opendkim.sock
SOCKET="local:/var/spool/postfix/opendkim/opendkim.sock" 
```


Upute Postfix-u da koristi OpenDKIM:
`sudo nano /etc/postfix/main.cf`
Na kraj dodati:
```
# Milter configuration
milter_default_action = accept
milter_protocol = 6
smtpd_milters = local:opendkim/opendkim.sock
non_smtpd_milters = $smtpd_milters
```

Zatim je potrebno povono pokrenuti oba servisa:
- `sudo systemctl restart opendkim`
- `sudo systemctl restart postfix`






##### 2.1.5 DMARC
######  2.1.5.1 OpenDMARC instalacija i konfiguracija


Instaliranje MySQL (server i klijent):
```
sudo apt update
sudo apt install mysql-server mysql-client -y
```

Instaliranje OpenDMARC:
- `sudo apt install opendmarc -y`

Kada se pojavi prozor u kojem traži odabir:
- Configure database? -> YES
- Password? -> ostaviti prazno (random password) -> OK
- Password za administratora? -> ostaviti prazno (random password) -> OK

Korisno je postaviti auto-start kod pokretanja (virtualnog) stroja:
- `sudo systemctl enable opendmarc`


Sada je potrebno urediti OpenDMARC konfiguracijsku datoteku:
- `sudo nano /etc/opendmarc.conf`


AuthservID postaviti na OpenDMARC:
```
AuthservID OpenDMARC
```

Dodati još:
```
TrustedAuthservIDs mail-server.lab
```

Zakomentirati stari socker i dodati novi:
```
#Socket local:/var/run/opendmarc/opendmarc.sock
Socket local:/var/spool/postfix/opendmarc/opendmarc.sock
```

Na kraj dodati:
```
RequiredHeaders true
SPFSelfValidate true
```




Potrebno je još dodati direktorij za socket file i urediti prava pristupa:
```
sudo mkdir -p /var/spool/postfix/opendmarc
sudo chown opendmarc:opendmarc /var/spool/postfix/opendmarc -R
sudo chmod 750 /var/spool/postfix/opendmarc/ -R
sudo adduser postfix opendmarc
```

Restart OpenDMARC da se primijene promijene:
- `sudo systemctl restart opendmarc`


######  2.1.5.2 Spajanje Postfix-a s OpenDMARC


Potrebno je urediti konfiguracijsku datoteku Postfix-a:
- `sudo nano /etc/postfix/main.cf`

Liniju `smtpd_milters = local:opendkim/opendkim.sock` treba promijeniti u:
 - `smtpd_milters = local:opendkim/opendkim.sock, local:opendmarc/opendmarc.sock`

Ponovo pokretanje Postfix-a, kako bi se primijenile promijene:
- `sudo systemctl restart postfix`

Kasnije kada se postavi Kali virtualni stroj i njegov mail server, tada će se testirati rad OpenDMARC-a na Ubuntu.


######  2.1.5.3 Dodavanje DMARC DNS TXT zapisa

Kako bi ispravno se testirao DMARC na Ubuntu, potrebno je dodati DMARC DNS TXT zapis u `kali-mail.lab` domenu.

Postavit će se slanje agregiranih i forenzičkih izvještaja na novog korisnika:
- `sudo adduser reports`


Uređivanje DNS zapisa:
- `sudo nano /etc/bind/db.mail-server.lab`


Potrebno je `Serial` povećati za 1 i na kraj dodati novi DNS TXT zapis
```
_dmarc IN TXT "v=DMARC1; p=quarantine; rua=mailto:reports@mail-server.lab; ruf=mailto:reports@mail-server.lab; fo=1"
```

Na kraju je potrebno ponovo pokrenuti BIND9 servis:
- `sudo systemctl restart bind9`
























### 2.2. Kali Linux

#### 2.2.1 Postfix (SMTP server)

Postavite hostname:
- `sudo hostnamectl set-hostname kali-mail.lab`

Urdite hostnames (statičku lokalnu DNS tablicu):
- `sudo nano /etc/hosts`
- Potrebno je dodati zapis:
- - `192.168.100.10 kali-mail.lab`

Instalacija Postfix-a:
- `sudo apt update`
- `sudo apt install postfix -y`

Prilikom instalacije Postifix-a odabrati:
- Opcija: `Internet Site`
- System mail name: `kali-mail.lab`

Provjera ako Postfix servis radi:
- `systemctl status postfix`
- Ponovo pokretanje (ponekad zatreba): 
- - `systemctl stop postfix`
- - `systemctl start postfix`

Instaliranje `mailutils`, za slanje test mailova:
- `sudo apt install mailutils -y`


#### 2.2.2 BIND9 (DNS server)
Potrebno je postaviti lokalni DNS server. Za to će se koristiti servis BIND9 (aka named).

Instalacija BIND9 (to je lokalni DNS)
- `sudo apt install bind9 -y`

Prvo je potrebno u mrežnim postavkama za oba mrežna sučelja postaviti da izričito koriste samo lokalni DNS server.

To se radi na način da se ode na:
 - Kali Linux ikonu (gore lijevo) -> gumb za postavke -> Advanced Network Configuration -> Wired connection 1 --> IPv4 Settings
   - Postaviti Method na `Automatic (DHCP) addresses only`
   - Postaviti DNS servers na `192.168.100.10`
   - Save
 - Kod Wired Connection 2 je potrebno:
   - postaviti DNS servers na `192.168.100.10`


Unijeti `sudo nmcli connection show`:
```
NAME                UUID                                  TYPE      DEVICE 
Wired connection 1  78898a07-6637-3d3c-8e77-6bdbd7414be9  ethernet  eth0   
Wired connection 2  12037b1a-e00e-32e5-8786-8ebf7814dd6a  ethernet  eth1   
lo                  cf8c1e89-51e0-42b5-beda-1db804e05c6a  loopback  lo 
```

Potrebno je identificirati NAME za eth0. Kada se zna NAME, mora se isključiti auto-dns:
```
sudo nmcli connection modify "Wired connection 1" ipv4.ignore-auto-dns yes
```


Unijeti 'ip a', i ako se slučajno pojavljuju dvije IP adrese na eth0 sučelju, potrebno je obrisati onu koja se prva stvorila ručno u ovim uputama:
```
sudo ip addr del 10.0.2.15/24 dev eth0
sudo systemctl restart NetworkManager
```


Unijeti još slijedeće komande:
```
sudo rm /etc/resolv.conf
sudo bash -c 'echo "nameserver 192.168.100.10" > /etc/resolv.conf'
sudo chattr +i /etc/resolv.conf
sudo systemctl restart NetworkManager
```

Ako se želi kasnije otključati mijenjanje: `sudo chattr -i /etc/resolv.conf`

- `cat /etc/resolv.conf`:

Trebalo bi biti:
```
nameserver 192.168.100.10

```



Konfiguracija BIND9 zona:

`sudo nano /etc/bind/named.conf.local`:

Mora izgledati ovako:
```
zone "kali-mail.lab" {
    type master;
    file "/etc/bind/db.kali-mail.lab";
};

zone "mail-server.lab" {
    type forward;
    forwarders { 192.168.100.50; };
};
```

`sudo nano /etc/bind/named.conf.options`:

Mora izgledati ovako:
```
options {
        directory "/var/cache/bind";
        allow-query {127.0.0.1; 192.168.100.0/24; };
        listen-on {127.0.0.1; 192.168.100.10; };
        allow-recursion { 127.0.0.1; 192.168.100.0/24; };
        recursion yes;
        forwarders {
                1.1.1.1;
                8.8.8.8;
        };
        dnssec-validation no;
};
```

Na kraju je potrebno restartati BIND DNS server:
- `sudo systemctl restart named`


#### 2.2.3 SPF

##### 2.2.3.1 Kreiranje SPF TXT zapisa


Uređivanje DNS zapisa:
- `sudo nano /etc/bind/db.kali-mail.lab`

Ovdje se postavljaju DNS zapisi i dodaje se SPF TXT zapis:
```
;
; BIND data file for local loopback interface
;
$TTL	604800
@	IN	SOA	kali-mail.lab. root.kali-mail.lab. (
			      2		; Serial
			 604800		; Refresh
			  86400		; Retry
			2419200		; Expire
			 604800 )	; Negative Cache TTL
;
@	IN	NS	kali-mail.lab.
@	IN	A	192.168.100.10
@	IN	TXT	"v=spf1 ip4:192.168.100.10 ~all"
```

Nakon promijene DNS zapisa, potrebno je ponovo pokrenuti BIND9 servis (Na kali Linux se taj servis naziva `named`).
- `sudo systemctl restart named`
- `sudo systemctl status named`


Testiranje:
`dig txt kali-mail.lab`:
```
;; ANSWER SECTION:
kali-mail.lab. 604800 IN TXT "v=spf1 ip4:192.168.100.10 ~all"
```

##### 2.2.3.2 Dodavanje SPF provjere dolaznim mailovima


Instalacije skripte za provjeru SPF-a:
- `sudo apt install postfix-policyd-spf-python`


Uređivanje Postfix servisa:

`sudo nano /etc/postfix/master.cf`

Na kraj je potrebno dodati:
```
policyd-spf unix - n n - 0 spawn user=policyd-spf argv=/usr/bin/policyd-spf
```

Uređivanje Postfix globalne konfiguracije:

 `sudo nano /etc/postfix/main.cf`

Potrebno je dodati na kraj:
```
policyd-spf_time_limit = 3600
smtpd_recipient_restrictions =
   permit_mynetworks,
   permit_sasl_authenticated,
   reject_unauth_destination,
   check_policy_service unix:private/policyd-spf
```

Zatim je potrebno ponovo pokrenuti Postfix servis kako bi se primijenile promijene:
- `sudo systemctl stop postfix`
- `sudo systemctl start postfix`

Sada će se u dolaznim mailovima raditi SPF provjera.


Ako nešto ne radi, osigurajte da su se ispravno proveli koraci o postavljanju lokalnih DNS servera...

##### 2.2.3.3 Testiranje rada SPF-a na oba Mail servera


**Testiranje rada razdvojenih DNS servera (split DNS)**:

Na Kali Linux treba raditi:
```
ping kali.org
ping mail-server.lab
```

Na Ubuntu treba raditi:
```
ping kali.org
ping kali-mail.lab
```


Sada kada su lokalni DNS serveri spremni, može se isprobati rad SPF-a.


**Ubuntu šalje, Kali prima**

Ovdje se testira ako Ubuntu ispravno poslužuje DNS TXT zapis za SPF i ako Kali ispravno radi provjeru SPF-a.

Na Ubuntu je potrebno poslati mail prema Kali ovako:
- `echo "Test SPF" | mail -s "SPF test" kali@kali-mail.lab`

Dobiveni mail na Kali sadrži (samo se unese komanda `mail` da se vide mailovi):
```
Received-SPF: Pass (mailfrom) identity=mailfrom; client-ip=192.168.100.50; helo=mail-server.lab; envelope-from=filip@mail-server.lab; receiver=kali-mail.lab
```


**Kali šalje, Ubuntu prima**


Na Kali je potrebno poslati mail prema Ubuntu ovako (potrebno je zamijeniti `filip` s odgovarajućim korisnikom):
- `echo "Test SPF" | mail -s "SPF test" filip@mail-server.lab`

Dobiveni mail na Ubuntu sadrži (samo se unese komanda `mail` da se vide mailovi):
```
Received-SPF: Pass (mailfrom) identity=mailfrom; client-ip=192.168.100.10; helo=kali-mail.lab; envelope-from=kali@kali-mail.lab; receiver=mail-server.lab
```

Time se potvrdilo da radi SPF na Ubuntu i na Kali Linux.




#### 2.2.4 DKIM
##### 2.2.4.1  DKIM instalacija i konfiguracija


Instalacija alata za DKIM:
- `sudo apt install opendkim opendkim-tools -y`

Dodaje korisnika postfix u grupu opendkim (potrebno zas ispravni rad):
- `sudo gpasswd -a postfix opendkim`


Konfiguriranje OpenDKIM-a:
`sudo nano /etc/opendkim.conf`:

Potrebno je odkomentirati Logwhy i postaviti na yes:
```
Logwhy yes
```

Ovaj dio urediti da izgleda ovako:
```
Canonicalization        relaxed/simple
Mode                    sv
SubDomains              no
```

Ispod SubDomains je potrebno dodati:
```
AutoRestart         yes
AutoRestartRate     10/1M
Background          yes
DNSTimeout          5
SignatureAlgorithm  rsa-sha256
```


Na kraju je još potrebno ovdje dodati:
```
Nameservers             127.0.0.1
```

Ne smije se dva puta pojavljivati zapis Nameservers, stoga je potrebno zakomentirati sve ostale Nameservers zapise...

I zakomentirati `TrustAnchorFile`:
```
#TrustAnchorFile                /usr/share/dns/root.key
```

Na čisti kraj dodati:

```
# Map domains in From addresses to keys used to sign messages
KeyTable           refile:/etc/opendkim/key.table
SigningTable       refile:/etc/opendkim/signing.table

# Hosts to ignore when verifying signatures
ExternalIgnoreList  /etc/opendkim/trusted.hosts

# A set of internal hosts whose mail should be signed
InternalHosts       /etc/opendkim/trusted.hosts
```



##### 2.2.4.2  DKIM ključevi

Sada je potrebno kreirati ključeve i tablice:
```
sudo mkdir /etc/opendkim
sudo mkdir /etc/opendkim/keys
sudo chown -R opendkim:opendkim /etc/opendkim
sudo chmod go-rw /etc/opendkim/keys
```

`sudo nano /etc/opendkim/signing.table`:
```
*@kali-mail.lab default._domainkey.kali-mail.lab
*@*.kali-mail.lab default._domainkey.kali-mail.lab
```

`sudo nano /etc/opendkim/key.table`:
```
default._domainkey.kali-mail.lab kali-mail.lab:default:/etc/opendkim/keys/kali-mail.lab/default.private
```

`sudo nano /etc/opendkim/trusted.hosts`:
```
127.0.0.1
::1
localhost
.kali-mail.lab
192.168.100.10
```


Kreiranje javnog i privatnog ključa:

```
sudo mkdir /etc/opendkim/keys/kali-mail.lab
sudo opendkim-genkey -b 2048 -d kali-mail.lab -D /etc/opendkim/keys/kali-mail.lab -s default -v
sudo chown opendkim:opendkim /etc/opendkim/keys/kali-mail.lab/default.private
sudo chmod 600 /etc/opendkim/keys/kali-mail.lab/default.private
```


Objavljivanje javnog ključa:
- `sudo cat /etc/opendkim/keys/kali-mail.lab/default.txt`

Iskopirati ovaj dio:
```
default._domainkey      IN      TXT     ( "v=DKIM1; h=sha256; k=rsa; "
          "p=MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA3EdIofls69BWoMAkeMDpgD85+uIfX825UaSFZKOBHeioJICWVvqf51lEtoKBQ1Prv/RlvsS9yg8zYrxa/kco3vt7ELOlIuVkA3RQbpxP5V//Apw2iw3iMOSe4QWcqdV7wnYkyZ4Eeaj8upMeHDhHMR8ZE5DbZvFddm10q7bTjvsV0wYBGWucstFqeFMjyNOTbDHpIX9cGT0j8P"
          "PgIQIVvs+8OwWvTy4ldEmfGiV6OodxwStNtCjzOneNvYqv6+HN3elT5OWs9l/3G8dtq5flKijsNJoNWEgcCHPoC171N4HA6NVf6c+vQrvET4d7oz2YYhVKyB6UkO1Q9YQ58uTY+wIDAQAB" )
```


Sada je potrebno urediti DNS zapise u BIND9:
`sudo nano /etc/bind/db.kali-mail.lab`:

Treba ovako izgledati (Serial povećati za 1, ukloniti razmake u vrijednosti DKIM TXT + razdvojiti stringove jer je max 255 znaka po stringu, sve u jednoj liniji OBAVEZNO):

```
;
; BIND data file for local loopback interface
;
$TTL	604800
@	IN	SOA	kali-mail.lab. root.kali-mail.lab. (
			      3		; Serial
			 604800		; Refresh
			  86400		; Retry
			2419200		; Expire
			 604800 )	; Negative Cache TTL
;
@	IN	NS	kali-mail.lab.
@	IN	A	192.168.100.10
@	IN	TXT	"v=spf1 ip4:192.168.100.10 ~all"

default._domainkey IN TXT ("v=DKIM1;h=sha256;k=rsa;" "p=MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA3EdIofls69BWoMAkeMDpgD85+uIfX825UaSFZKOBHeioJICWVv" "qf51lEtoKBQ1Prv/RlvsS9yg8zYrxa/kco3vt7ELOlIuVkA3RQbpxP5V//Apw2iw3iMOSe4QWcqdV7wnYkyZ4Eeaj8upMeHDhHMR8ZE5DbZvFddm10q7bTjvsV0wYBGWucstFqeFMjyNOTbDHpIX9cGT0j8P" "PgIQIVvs+8OwWvTy4ldEmfGiV6OodxwStNtCjzOneNvYqv6+HN3elT5OWs9l/3G8dtq5flKijsNJoNWEgcCHPoC171N4HA6NVf6c+vQrvET4d7oz2YYhVKyB6UkO1Q9YQ58uTY+wIDAQAB")

```

Zatim restart BIND9:
- `sudo systemctl restart named`
- `sudo systemctl status named`



Potrebno je ponovo pokrenuti opendkim servis:
- `sudo systemctl restart opendkim`


Testiranje opendkim ključeva:
-`sudo opendkim-testkey -d kali-mail.lab -s default -vvv`
- U ispisu bi se trebalo na kraju vidjeti `key OK`



##### 2.2.4.3 Spajanje Postfix sa OpenDKIM

Stvoriti direktorij u kojem će se postaviti Socket za komunikaciju Postfix <-> OpenDKIM:
```
sudo mkdir -p /var/spool/postfix/opendkim
sudo chown opendkim:postfix /var/spool/postfix/opendkim
```

Uređivanje konfiguracije OpenDKIM-a:
`sudo nano /etc/opendkim.conf`

Dio sa socketima mora se promijniti u ovo:
```
#Socket			local:/run/opendkim/opendkim.sock
#Socket			inet:8891@localhost
#Socket			inet:8891
Socket			local:/var/spool/postfix/opendkim/opendkim.sock
```

`sudo nano /etc/default/opendkim`:
Zakomentirati stari SOCKET i staviti novi:
```
#SOCKET=local:$RUNDIR/opendkim.sock
SOCKET="local:/var/spool/postfix/opendkim/opendkim.sock" 
```


Upute Postfix-u da koristi OpenDKIM:
`sudo nano /etc/postfix/main.cf`
Na kraj dodati:
```
# Milter configuration
milter_default_action = accept
milter_protocol = 6
smtpd_milters = local:opendkim/opendkim.sock
non_smtpd_milters = $smtpd_milters
```

Zatim je potrebno povono pokrenuti oba servisa:
- `sudo systemctl restart opendkim`
- `sudo systemctl restart postfix`


##### 2.2.4.4 Testiranje DKIM

**Ubuntu šalje, Kali prima**

Na Ubuntu: `echo "Test DKIM" | mail -s "DKIM test" kali@kali-mail.lab`

Kali prima:
```
Authentication-Results: kali-mail.lab;
        dkim=pass (2048-bit key; unprotected) header.d=mail-server.lab header.i=@mail-server.lab header.a=rsa-sha256 header.s=default header.b=DKHQeWjg;
        dkim-atps=neutral

DKIM-Signature: v=1; a=rsa-sha256; c=relaxed/simple; d=mail-server.lab;
        s=default; t=1767203633;
        bh=+qlNhYuQiot52MMJ53YSV0rt4q35P6JeHyKLUgbd7Ek=;
        h=Subject:To:Date:From:From;
        b=l/p/QVpjTx5cRGuozDDq2aWlkQlX996lOSoweipDZMfcFnug3DnHQXYe4UGg/ip+4
         li96BtO2iNto1ulQmc3SdF6cqVkWUakn8fYu/ZsG44BZgFXbBIZhVYC69pzDetIlvG
         W7BUM2+HNiNUfuw+CtolSxZBFCoWNOCLN087O3kOPeO2mvaFVpm3Q+VL6VY+nB4/HU
         WC3m8rZ9rzuXWlogDBqj2IyVMS0jCGmYDvKGmsJWNxm1tuhseekE7kXEScb81Y84Ym
         jZ1WIA4lZKrjyam2/j+XgMa8YRV9FNueKdJCikHopRxM+STGBP2RYr3mql89o148V3
         KXb6QJtkGrWgQ==
```


**Ubuntu šalje, Kali prima**

Na Kali (paziti da se postavi točan korisnik): `echo "Test DKIM" | mail -s "DKIM test" filip@mail-server.lab`

Ubuntu prima:
```
Authentication-Results: mail-server.lab;
	dkim=pass (2048-bit key; unprotected) header.d=kali-mail.lab header.i=@kali-mail.lab header.a=rsa-sha256 header.s=default header.b=N0RyYhr7;
	dkim-atps=neutral

DKIM-Signature: v=1; a=rsa-sha256; c=relaxed/simple; d=kali-mail.lab;
	s=default; t=1767202638;
	bh=+qlNhYuQiot52MMJ53YSV0rt4q35P6JeHyKLUgbd7Ek=;
	h=Subject:To:Date:From:From;
	b=N0RyYhr70feoJ+wxpC5GhcoE91hr5dRA0r30N5lDp9RUbEUmi/JCEUTY4z2SNJtMd
	 vnXJVhjvzikbbEm0/xQXDOojOmXXV1Nh06j1lTap2OrdA1gtW/ecn9Nd22qKyKCSA6
	 NJ+afycP8Ao9jAjxQhqAG5lHt8Kj2uB51Gn4Vv6QFAkZRw9S5LcoGo2Rmuei8TSZ1m
	 4obK+uKZpxrj2B2bpxmcdwJo0yUwIHxGo/xHEofridDetox+IM/xq6ogbpzLE7QdKA
	 qaxDZYK1ON+LJMIG1xSJ/owxor1MxBxsZWYxOUNWCgpkHRSy/2dCUHTY4iKy/yqk66
	 gYHnMF+r/0LZw==
```

##### 2.2.5 DMARC
######  2.2.5.1 OpenDMARC instalacija i konfiguracija


Pokretanje MySQL (več je po defaultu instalirano na Kali):
```
sudo systemctl start mysql
sudo systemctl status mysql

```
Instaliranje OpenDMARC:
- `sudo apt install opendmarc -y`

Kada se pojavi prozor u kojem traži odabir:
- Configure database? -> YES
- Password? -> ostaviti prazno (random password) -> OK
- Password za administratora? -> ostaviti prazno (random password) -> OK

Korisno je postaviti auto-start kod pokretanja (virtualnog) stroja:
- `sudo systemctl enable opendmarc`


Sada je potrebno urediti OpenDMARC konfiguracijsku datoteku:
- `sudo nano /etc/opendmarc.conf`


AuthservID postaviti na OpenDMARC:
```
AuthservID OpenDMARC
```

Dodati još:
```
TrustedAuthservIDs mail-server.lab
```

Zakomentirati stari socker i dodati novi:
```
#Socket local:/var/run/opendmarc/opendmarc.sock
Socket local:/var/spool/postfix/opendmarc/opendmarc.sock
```

Na kraj dodati:
```
RequiredHeaders true
SPFSelfValidate true
```


Potrebno je još dodati direktorij za socket file i urediti prava pristupa:
```
sudo mkdir -p /var/spool/postfix/opendmarc
sudo chown opendmarc:opendmarc /var/spool/postfix/opendmarc -R
sudo chmod 750 /var/spool/postfix/opendmarc/ -R
sudo adduser postfix opendmarc
```

Restart OpenDMARC da se primijene promijene:
- `sudo systemctl restart opendmarc`


######  2.2.5.2 Spajanje Postfix-a s OpenDMARC


Potrebno je urediti konfiguracijsku datoteku Postfix-a:
- `sudo nano /etc/postfix/main.cf`

Liniju `smtpd_milters = local:opendkim/opendkim.sock` treba promijeniti u:
 - `smtpd_milters = local:opendkim/opendkim.sock, local:opendmarc/opendmarc.sock`

Ponovo pokretanje Postfix-a, kako bi se primijenile promijene:
- `sudo systemctl restart postfix`


###### 2.2.5.3 DMARC DNS TXT zapis

Kako bi ispravno se testirao DMARC na Ubuntu, potrebno je dodati DMARC DNS TXT zapis u `kali-mail.lab` domenu.

Urešivanje DNS zapisa:
- `sudo nano /etc/bind/db.kali-mail.lab`


Potrebno je `Serial` povećati za 1 i na kraj dodati novi DNS TXT zapis
```
_dmarc IN TXT "v=DMARC1; p=quarantine; rua=mailto:kali@kali-mail.lab; ruf=mailto:kali@kali-mail.lab; fo=1"

```

Na kraju je potrebno ponovo pokrenuti BIND9 servis:
- `sudo systemctl restart named`











## 3. Testiranje OpenDMARC

### 3.1 Testiranje slanja mailova


Na Kali Linux se šalje ispravni email:
- `echo "Test DMARC" | mail -s "DMARC test" filip@mail-server.lab`


Ako ne radi slanje mailovau, provjerite da IP adrese nisu nestale s mrežnih sučelja pomoću `ip a`.
Ako jesu, tada se može isprobati:
- Na Kali: `sudo ip addr add 192.168.100.10/24 dev eth1` + `sudo systemctl restart NetworkManager`
- Na Ubuntu: Provjera ručno postavljanje statične IP adrese preko GUI + `sudo systemctl restart NetworkManager`

Također provjerite da na oba virtualna stroja radi:
- `sudo systemctl status postfix`
- `sudo systemctl status opendkim`

I ako na Ubuntu radi:
- `sudo systemctl status opendmarc`


Ako provjere padaju:
- Ubuntu: `sudo systemctl status bind9`
- Kali: `sudo systemctl status named`



Ako sve radi, u mailu se može vidjeti informacija o DMARC provjeri:
```
Authentication-Results: OpenDMARC; dmarc=pass (p=none dis=none) header.from=kali-mail.lab
```


**Spoofanje mail-a**

Ovdje će se pokušati poslati spoofani email koji bi trebao pasti DMARC provjeru.

Na Kali:
- `echo "Ovo je test za DMARC." | mail -s "DMARC test" -r alice@mail-server.lab bob@mail-server.lab`

Pričekajte 5-10 sekunda.

Na Ubuntu:
- `su - bob`
- `mail`
- Unijeti: `1`

Sada se vidi:
```
Authentication-Results: OpenDMARC; dmarc=fail (p=quarantine dis=none) header.from=mail-server.lab
```

## Dovecot

Dovecot je:
- IMAP/POP3 server koji omogućuje korisnicima pristup e-pošti spremljenoj na mail serveru  
- zadužen za autentikaciju korisnika i upravljanje mailbox-ovima 

Koristit će se thunderbird da se pokaže rad Dovecota.


**Ubuntu**

Instaliranje Dovecot-a:
```
sudo apt install dovecot-core dovecot-imapd dovecot-pop3d -y
sudo systemctl enable dovecot
````

Instaliranje Thunderbird-a:
 - `sudo apt install thunderbird`

Pokretanje: `tunderbird` ili ikona lijevo u izborniku.




Postavljanje lokalnog mail korisnika:
<p align="center">
 <a href="https://github.com/user-attachments/assets/01908360-585b-43bb-a7da-a48c24a3e9aa?raw=true" target="_blank">
  <img src="https://github.com/user-attachments/assets/01908360-585b-43bb-a7da-a48c24a3e9aa" width="400"/>
  <a/>
<p/>


Odabire se IMAP
<p align="center">
 <a href="https://github.com/user-attachments/assets/a0129afc-f53a-4c9e-b86a-1dbc30e2748e?raw=true" target="_blank">
  <img src="https://github.com/user-attachments/assets/a0129afc-f53a-4c9e-b86a-1dbc30e2748e" width="400"/>
  <a/>
<p/>


Razlika IMAP i POP3 je:
- IMAP ostavlja poruke na serveru i sinkronizira ih između više uređaja  
- POP3 preuzima poruke na klijent i obično ih briše sa servera  
- IMAP je pogodniji za modernu upotrebu i mail klijente poput Thunderbird-a


Istiniti mail (u Kali CLI): `echo "Pozdrav LP" | mail -s "Thunderbird Test" filip@mail-server.lab`

<p align="center">
 <a href="https://github.com/user-attachments/assets/b88b30fc-9cde-4518-9d73-e914301b33dd?raw=true" target="_blank">
  <img src="https://github.com/user-attachments/assets/b88b30fc-9cde-4518-9d73-e914301b33dd"/>
  <a/>
<p/>


Spoofani mail (u Kali CLI): `echo "Pozdrav LP" | mail -s "Thunderbird Test" -r alice@mail-server.lab filip@mail-server.lab`

<p align="center">
 <a href="https://github.com/user-attachments/assets/c9e4ce06-7695-4042-88f5-18995dddb417?raw=true" target="_blank">
  <img src="https://github.com/user-attachments/assets/c9e4ce06-7695-4042-88f5-18995dddb417"/>
  <a/>
<p/>


Vidi se kako su oba maila pristigla u Inbox makar je drugi mail imao neuspjele provjere (dmarc=fail).
Stoga je ovdje potrebno načiniti neke izmjene da bi se povećala sigurnost mail servera.





## 4. IZVORI
- https://www.linkedin.com/pulse/how-build-your-own-email-server-ubuntu-part-4-liviu-gelca-gda0e
- https://askubuntu.com/questions/965343/enabling-and-disabling-network-card-through-commandline
- https://serverfault.com/questions/1021262/whats-the-right-way-to-enter-dkim-string-into-bind-zone-file
- https://stackoverflow.com/questions/43720476/setting-up-dkim-setup-dns-zone-syntax-error-on-bind-in-ubuntu
- https://support.dnsimple.com/articles/txt-record-format/
- https://blog.matrixpost.net/set-up-dmarc-for-postfix-on-ubuntu/
- https://www.linuxbabe.com/mail-server/create-dmarc-record
- https://www.server-world.info/en/note?os=CentOS_Stream_9&p=dns&f=10
- https://dovecot.org/
- https://www.thunderbird.net/en-US/
