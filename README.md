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

<span style="color: lightgray">email;</span> <span style="color: red"><em>testi@testi.fi</em></span> <span style="color: lightgray">;password;</span> <span style="color: red"><em>insertPasswordHere</em></span>

Tämän jälkeen riveille 9, 10 ja 11 tulee asettaa oikeat polut. 

**HUOM: pythoniin voi merkitä tiedoston polun monella eri tavalla. Pidä huoli, että polut on merkitty oikein. Alla on
esimerkit kolmesta erilaisesta merkintätavasta.**

```python
file_path = "C:/file/path/here"
file_path = "C:\\file\\path\\here"
file_path = r"C:\file\path\here"
```

Riville 9 asetetaan polku tiedostolle _login.txt_, jonka olet juuri kloonannut repositoriosta.

```python

login_file_path = r"C:/.../login.txt", "r"

```

Seuraavaksi riville 10 tulee asettaa kansion polku, johon Chrome on asetettu tallentamaan uudet tiedostot (yleensä _Downloads_ kansio).

```python

downloads_path = r"C:/Users/_nameHere_/Downloads/*"

```

Viimeisenä muutoksena tulee määritellä tiedosto, johon käsitelty, valmis data tallennetaan. Itse olen esim. luonut _kulukorvaukset.txt_ tiedoston omaan
_Hallitus_ kansiooni ja liittänyt tämän tiedoston polun koodiin. Tämä tapahtuu rivillä 11.

```python

kulukorvaukset_path = r"C:/.../Hallitus/kulukorvaukset.txt"

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


