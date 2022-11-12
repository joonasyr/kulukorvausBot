# **kulukorvaus-scripti/botti**

## Toiminnot

Kyseessä on botti joka automatisoi kulukorvausten hakemisen [kululaskut.fi](https://kululaskut.fi/) sivustolta.

Botti kirjautuu itse määritellyillä tunniksilla sivustolle, hakee uudet kulukorvaukset viimeisen 30 päivän sisällä,
lataa niistä CSV tiedoston ja lopuksi uudelleenkirjoittaa CSV tiedoston käytettävän datan tekstimuotoon, jonka
voi kopioida suoraan kokouksen virtuaaliseen esityslistaan.

### _Miksi?_

Helpottamaan rahastonhoitajan / rahastonhoitajan avun elämää. Kulukorvausten liittäminen VEL:iin manuaalisesti on
puuduttavaa hommaa.

## Käyttöohjeet

Ensimmäiseksi tulee vaihtaa oikeat kirjautumistiedot _login.txt_ tiedostoon. Riville 11 ja 18 tulee asettaa hakemiston osoite,
johon tiedosto on koneellasi asennettu.

```python

login_file = open(r"C:\...", "r")

```

Seuraavaksi riville 66 tulee asettaa hakemisto, johon Chrome on asetettu tallentamaan ladatut tiedostot (yleensä _Downloads_ kansio).

```python

downloads = glob.glob("C:\\Users\\joona\\Downloads\\*".format(getpass.getuser()))

```

Viimeisenä muutoksena tulee määritellä tiedosto, johon käsitelty tieto tallennetaan. Itse olen esim. luonut _kulukorvaukset.txt_ tiedoston _Hallitus_ kansioon
ja liittänyt tämän osoitteen koodiin. Tämä tapahtuu riveillä 88 ja 93

```python

file = open(r"C:\...\Hallitus\kulukorvaukset.txt", "w")
.
.
.
os.startfile(r"C:\...\Hallitus\kulukorvaukset.txt")

```