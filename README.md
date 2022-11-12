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

Ensimmäiseksi tulee vaihtaa oikeat kirjautumistiedot login.txt tiedostoon. Riville 11 tulee asettaa oikea hakemiston
osoite.

```python

login_file = open(r"C:\Users\joona\PycharmProjects\kulukorvaus_projekti\login", "r")

```

Jotta ohjelma saadaan toimimaan oikein, tulee muutamalle riville asettaa/vaihtaa oikeat hakemistoreitit.
