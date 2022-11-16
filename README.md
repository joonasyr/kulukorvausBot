# kulukorvaus-scripti/botti

**NOTE: this _README_ is only in Finnish, as the script is only used by Tite's treasurers and/or assistant treasurers
that are required to speak fluent Finnish.**

## Yleistä

Kyseessä on scripti joka automatisoi kulukorvausten hakemisen [kululaskut.fi](https://kululaskut.fi/) sivustolta.

Ohjelma kirjautuu itse määritellyillä tunniksilla sivustolle, hakee uudet kulukorvaukset viimeisen 30 päivän sisällä,
lataa niistä CSV tiedoston ja lopuksi uudelleenkirjoittaa CSV tiedoston käytettävän datan tekstimuotoon, jonka
voi kopioida suoraan seuraavan kokouksen esityslistaan.

### _Miksi?_

Helpottamaan rahastonhoitajan / rahastonhoitajan avun elämää. Kulukorvausten liittäminen VEL:iin manuaalisesti on
puuduttavaa hommaa. Tällä säästää kallisarvoisia minuutteja joka viikko!

Lisäksi halusin tutustua seleniumiin, erilaisten toimintojen automatisointiin ja palautella mieleen Pythonia.

## Asennus

Ensimmäiseksi tulee vaihtaa oikeat kirjautumistiedot _login.txt_ tiedostoon. 

$${\color{lightgray}email; \color{red}testi@testi.fi \color{lightgray};password; \color{red}insertPasswordHere}$$

Tämän jälkeen riveille 11 ja 17 tulee asettaa polku tiedostolle _login.txt_, jonka olet kloonannut repositoriosta.

```python

with open("C:\\...\\login", "r") as login_file:

```
**HUOM: pythoniin voi merkitä tiedoston polun monella eri tavalla. Pidä huoli, että polut on merkitty oikein. Alla on
esimerkit kolmesta erilaisesta merkintätavasta.**

```python
file_path = "C:/file/path/here"
file_path = "C:\\file\\path\\here"
file_path = r"C:\file\path\here"
```
Jatketaan. Seuraavaksi riville 64 tulee asettaa kansion polku, johon Chrome on asetettu tallentamaan uudet tiedostot (yleensä _Downloads_ kansio).

```python

downloads = glob.glob("C:\\Users\\_nameHere_\\Downloads\\*".format(getpass.getuser()))

```

Viimeisenä muutoksena tulee määritellä tiedosto, johon käsitelty tieto tallennetaan. Itse olen esim. luonut _kulukorvaukset.txt_ tiedoston _Hallitus_ kansioon
ja liittänyt tämän tiedoston polun koodiin. Tämä tapahtuu riveillä 85 ja 89

```python

with open("C:\\...\\Hallitus\\kulukorvaukset.txt", "w") as file:
.
.
.
os.startfile("C:\\...\\Hallitus\\kulukorvaukset.txt")

```

### .exe tiedoston luominen

Jotta scripti olisi mahdollisimman vaivaton ajaa, kannattaa yllä olevien muutosten jälkeen muuttaa koodi helposti ajettavaksi _.exe_ tiedostoksi.
Tämä tapahtuu helpoiten ***pyinstallerin*** kautta. 

**HUOM**: tässä vaiheessa oletan, että koneellasi on Python asennettuna.

Ensimmäisenä ***asennetaan pyinstaller***.  Avataan siis komentorivi ja kirjoitetaan

`pip install pyinstaller`

Seuraavaksi tulee ***asentaa*** scriptiin liittyvät ***kirjastot***.

`pip install selenium`

`pip install webdriver_manager`

`pip install packaging`

Ennen _.exe_ tiedostoksi muuttamista, kannattaa tässä vaiheessa ***testata, että koodi toimii oikein*** komentorivin kautta. Navigoi siis komentorivillä
kansioon, johon _kulukorvaus.py_ on tallenettu ja aja komento

`python kulukorvaus.py`		

Jos scripti toimi oikein, voidaan jatkaa eteenpäin. Seuraavaksi siirry komentorivillä kansioon, jossa _kulukorvaus.py_ sijaitsee  (jos et ole jo)
ja aja seuraava komento

`pyinstaller --onefile kulukorvaus.py`

Tämän komennon suoritettuasi loppuun pitäisi äskeiseen kansioon ilmestyä lisää tiedostoja. Uudessa _dist_ kansiossa sijaitsee nyt _kulukorvaus.exe_, jonka voit siirtää
esim. työpöydällesi. Jatkossa voit siis ajaa ohjelman suoraan työpöydältäsi.

## Huomioitavaa

Ohjelma on tarkoitettu ***apuvälineeksi***. Muista aina ***varmistaa*** vielä ***manuaalisesti*** [kululaskut.fi](https://kululaskut.fi/):stä, että kaikki uudet
kulukorvaukset on otettu huomioon.

Ohjelmassa ei ole kattavaa virhetarkastelua joten jos ohjelma kaatuu (varsinkin ensimmäisillä käyttökerroilla), kannattaa tarkistaa että muokkaamasi hakemistojen osoitteet
on kirjoitettu oikein.

_login.txt_ tiedoston sisältö ei ole mitenkään salattua, joten suosittelen käyttämään salasanana jotain salasanaa, joka ei ole sinulla muualla käytössä.
Jos salasana jostain syystä päätyisi vääriin käsiin, ei mitään radikaalia voi tapahtua. Kululaskut palvelussa ei onneksi saa mitään vakavaa tuhoa aikaan vaikka sinne joku
ulkopuolinen pääsisikin.

Ohjelma on ja ohjeet on suunnattu vain Windows pohjaisille käyttöjärjestelmille. Jos käytät Linuxia tai MacOS pohjaista konetta, saatat joutua hieman soveltamaan.


