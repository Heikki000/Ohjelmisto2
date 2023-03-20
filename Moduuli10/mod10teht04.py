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


class Auto:
    auto_count = 0
    def __init__(self, rekisteritunnus, huippunopeus):
        Auto.auto_count += 1
        #print(f"{Auto.auto_count}. Uusi auto luotu, rekisteri: {rekisteritunnus} ja huippunopeus {huippunopeus} km/h.")
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.matka = 0

    def kiihdytä(self, muutos):
        if muutos < 0:
            while self.nopeus > 0 and muutos <= 0:
                muutos += 1
                self.nopeus -= 1
        else:
            while self.nopeus < self.huippunopeus and muutos > 0:
                muutos -= 1
                self.nopeus += 1

    def kulje(self, aika):
            self.matka = self.matka + aika * self.nopeus
            return self.matka


    def tiedot(self):
        print(f"Auton rekisteritunnus on {self.rekisteritunnus}, huippunopeus {self.huippunopeus} km/h, "
              f"tämänhetkinen nopeus {self.nopeus} km/h ja kuljettu matka {self.matka:.0f} km.")

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
            if auto.matka >= self.pituus:
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
    for n in range(10):
        kilpailu.tunti_kuluu()
        if kilpailu.kilpailu_ohi() == True:
            break

'''
game = True
while game == True:
    for auto in autot:
        if auto.matka >= 10000:
            print("-------------------------------")
            print(f"Auto {auto.rekisteritunnus} on saavuttanut 1000 km:n matkan ja voitti kilpailun!\n")
            game = False
            break
        else:
            auto.kiihdytä(random.randint(-10, 15))
            auto.kulje(1)
            #auto.tiedot()  testaamista varten
print("|Rekisteritunnus|  Huippunopeus |  Loppunopeus  | Kokonaismatka |")
for auto in autot:
    print(f"|{auto.rekisteritunnus:^{15}}|{auto.huippunopeus:^{15}}|{auto.nopeus:^{15}}|{auto.matka:^{15}}|")'''