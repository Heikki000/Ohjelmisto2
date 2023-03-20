'''
Tehtävä on jatkoa aiemmalle autokilpailutehtävälle. Kirjoita Kilpailu-luokka, jolla on ominaisuuksina kilpailun
nimi, pituus kilometreinä ja osallistuvien autojen lista. Luokassa on alustaja, joka saa parametreinaan nimen,
kilometrimäärän ja autolistan ja asettaa ne ominaisuuksille arvoiksi. Luokassa on seuraavat metodit:

tunti_kuluu, joka toteuttaa aiemmassa autokilpailutehtävässä mainitut tunnin välein tehtävät toimenpiteet
eli arpoo kunkin auton nopeuden muutoksen ja kutsuu kullekin autolle kulje-metodia.
tulosta_tilanne, joka tulostaa kaikkien autojen sen hetkiset tiedot selkeäksi taulukoksi muotoiltuna.
kilpailu_ohi, joka palauttaa True, jos jokin autoista on maalissa eli se on ajanut vähintään kilpailun
kokonaiskilometrimäärän. Muussa tapauksessa palautetaan False.
Kirjoita pääohjelma, joka luo 8000 kilometrin kilpailun nimeltä "Suuri romuralli".
Luotavalle kilpailulle annetaan kymmenen auton lista samaan tapaan kuin aiemmassa tehtävässä.
Pääohjelma simuloi kilpailun etenemistä kutsumalla toistorakenteessa tunti_kuluu-metodia,
jonka jälkeen aina tarkistetaan kilpailu_ohi-metodin avulla, onko kilpailu ohi.
Ajantasainen tilanne tulostetaan tulosta tilanne-metodin avulla kymmenen tunnin välein sekä kertaalleen sen jälkeen, kun kilpailu on päättynyt.
'''
import random
from time import sleep

class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.matka = 0

    def kiihdytä(self, muutos):
        self.nopeus += muutos
        if self.nopeus < 0:
            self.nopeus = 0
        elif self.nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus

    def kulje(self, aika):
        self.matka = self.matka + aika * self.nopeus
        return


    #def tiedot(self):
     #   print(f"Auton rekisteritunnus on {self.rekisteritunnus}, huippunopeus {self.huippunopeus} km/h, "
      #        f"tämänhetkinen nopeus {self.nopeus} km/h ja kuljettu matka {self.matka:.0f} km.")

class Kilpailu:
    def __init__(self, nimi, pituus, auto_lista):
        self.nimi = nimi
        self.pituus = pituus
        self.auto_lista = []
        for n in range(1, auto_lista + 1):
            auto = Auto("ABC-" + str(n), random.randint(100, 200))
            self.auto_lista.append(auto)

    def tunti_kuluu(self):
        for auto in self.auto_lista:
            auto.kiihdytä(random.randint(-10, 15))
            auto.kulje(1)

    def tulosta_tilanne(self):
        print("-----------------------------------------------------------------")
        print("|Rekisteritunnus|  Huippunopeus |    Nopeus     | Kokonaismatka |")
        for auto in self.auto_lista:
            print(f"|{auto.rekisteritunnus:^{15}}|{auto.huippunopeus:^{15}}|{auto.nopeus:^{15}}|{auto.matka:^{15}}|")

    def kilpailu_ohi(self):
        for auto in self.auto_lista:
            if auto.matka > self.pituus:
                return True
        else:
            return False


kilpailu = Kilpailu('Suuri romuralli', 8000, 10)

while True:
    if kilpailu.kilpailu_ohi() == True:
        print(f"\n!!KILPAILU PÄÄTTYI!!!")
        kilpailu.tulosta_tilanne()
        break
    kilpailu.tulosta_tilanne()
    sleep(0.5)
    for n in range(10):
        kilpailu.tunti_kuluu()
        if kilpailu.kilpailu_ohi() == True:
            break
