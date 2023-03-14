'''
Jatka ohjelmaa kirjoittamalla Auto-luokkaan kiihdytä-metodi, joka saa
parametrinaan nopeuden muutoksen (km/h). Jos nopeuden muutos on negatiivinen,
auto hidastaa. Metodin on muutettava auto-olion nopeus-ominaisuuden arvoa.
Auton nopeus ei saa kasvaa huippunopeutta suuremmaksi eikä alentua nollaa pienemmäksi.
Jatka pääohjelmaa siten, että auton nopeutta nostetaan ensin +30 km/h, sitten +70 km/h
ja lopuksi +50 km/h. Tulosta tämän jälkeen auton nopeus. Tee sitten hätäjarrutus määräämällä
nopeuden muutos -200 km/h ja tulosta uusi nopeus. Kuljettua matkaa ei tarvitse vielä päivittää.
'''


class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.matka = 0

    def kiihdytys(self, muutos):
        if muutos < 0:
            while self.nopeus > 0 and muutos <= 0:
                muutos += 1
                self.nopeus -= 1
        else:
            while self.nopeus < self.huippunopeus and muutos >= 0:
                muutos -= 1
                self.nopeus += 1

    def tiedot(self):
        print(f"Auton rekisteritunnus on {self.rekisteritunnus}, huippunopeus {self.huippunopeus} km/h, "
              f"tämänhetkinen nopeus {self.nopeus} km/h ja kuljettu matka {self.matka:.0f} km.")

auto_1 = Auto("ABC-123", 145)

auto_1.tiedot()
auto_1.kiihdytys(30)
auto_1.kiihdytys(70)
auto_1.kiihdytys(50)
print(f"Auton nopeus on {auto_1.nopeus} km/h.")
auto_1.kiihdytys(-200)
print(f"Auton nopeus on {auto_1.nopeus} km/h.")
# print(f"Auton rekisteritunnus on {auto_1.rekisteritunnus}") tämä muistutuksena, miten printataan suoraan
