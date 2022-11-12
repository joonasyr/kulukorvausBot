# kulukorvaus-scripti/botti

**NOTE: this _README_ is only in Finnish, as the script is used by only Tite's treasurers and/or assistant treasurers that are required to speak fluent Finnish.

## Toiminnot

Kyseessä on botti joka automatisoi kulukorvausten hakemisen [kululaskut.fi](https://kululaskut.fi/) sivustolta.

Botti kirjautuu itse määritellyillä tunniksilla sivustolle, hakee uudet kulukorvaukset viimeisen 30 päivän sisällä,
lataa niistä CSV tiedoston ja lopuksi uudelleenkirjoittaa CSV tiedoston käytettävän datan tekstimuotoon, jonka
voi kopioida suoraan kokouksen virtuaaliseen esityslistaan.

### _Miksi?_

Helpottamaan rahastonhoitajan / rahastonhoitajan avun elämää. Kulukorvausten liittäminen VEL:iin manuaalisesti on
puuduttavaa hommaa.

## Käyttöohjeet

Ensimmäiseksi tulee vaihtaa oikeat kirjautumistiedot _login.txt_ tiedostoon. 

$${\color{lightgray}email; \color{red}testi@testi.fi \color{lightgray};password; \color{red}insertPasswordHere}$$

Tämän jälkeen riville 11 ja 18 tulee asettaa hakemiston osoite,
johon kyseinen tiedosto on koneellasi asennettu.

```python

login_file = open(r"C:\...", "r")

```

Seuraavaksi riville 66 tulee asettaa hakemiston osoite, johon Chrome on asetettu tallentamaan uudet tiedostot (yleensä _Downloads_ kansio).

```python

downloads = glob.glob("C:\\Users\\joona\\Downloads\\*".format(getpass.getuser()))

```

Viimeisenä muutoksena tulee määritellä tiedosto, johon käsitelty tieto tallennetaan. Itse olen esim. luonut _kulukorvaukset.txt_ tiedoston _Hallitus_ kansioon
ja liittänyt tämän tiedoston osoitteen koodiin. Tämä tapahtuu riveillä 88 ja 93

```python

file = open(r"C:\...\Hallitus\kulukorvaukset.txt", "w")
.
.
.
os.startfile(r"C:\...\Hallitus\kulukorvaukset.txt")

```

### .exe tiedoston luominen

Jotta scripti olisi mahdollisimman vaivaton ajaa, on järkevää yllä olevien muutosten jälkeen muuttaa koodi ajettavaksi _.exe_ tiedostoksi.
Tämä tapahtuu helpoiten ***pyinstallerin*** kautta. ***HUOM*** tässä vaiheessa oletan, että  koneellasi on jo Python asennettuna.

Ensimmäisenä ***asennetaan pyinstaller***.  Avataan siis komentorivi ja kirjoitetaan

`pip install pyinstaller`

Seuraavaksi tulee asentaa scriptiin liittyvät kirjastot.

`pip install selenium`

`pip install webdriver_manager`

`pip install packaging`

Ennen _.exe_ tiedostoksi muuttamista, kannattaa tässä vaiheessa kokeilla, että koodi toimii oikein komentorivin kautta. Navigoi siis komentorivillä
kansioon, johon _main.py_ on tallenettu ja aja komento

`python main.py`		

Jos scripti toimi oikein, voidaan jatkaa eteenpäin. Seuraavaksi siirry komentorivillä kansioon, jossa _main.py_ sijaitsee  (jos et ole jo)
ja aja seuraava komento

`pyinstaller --onefile main.py`

Tämän komennon suoritettuasi äskeiseen kansioon on nyt tullut lisää tiedostoja. Uudessa _dist_ kansiossa sijaitsee nyt _main.exe_, jonka voit siirtää
esim. työpöydällesi valmiiksi käyttöä varten.

## Huomioitavaa

Ohjelmassa ei ole virhetarkastelua joten jos ohjelma kaatuu (varsinkin ensimmäsillä käyttökerroilla), kannattaa tarkistaa että muokatut hakemistojen osoitteet
on kirjoitettu oikein.

Ohjelma on tarkoitettu ***apuvälineeksi***. Muista aina ***varmistaa*** vielä ***manuaalisesti*** [kululaskut.fi](https://kululaskut.fi/):stä, että kaikki uudet
kulukorvaukset on saatu mukaan.


