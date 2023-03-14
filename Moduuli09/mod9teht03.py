'''
Laajenna ohjelmaa siten, että mukana on kulje-metodi, joka saa parametrinaan tuntimäärän.
Metodi kasvattaa kuljettua matkaa sen verran kuin auto on tasaisella vauhdilla annetussa
tuntimäärässä edennyt. Esimerkki: auto-olion tämänhetkinen kuljettu matka on 2000 km.
Nopeus on 60 km/h. Metodikutsu auto.kulje(1.5) kasvattaa kuljetun matkan lukemaan 2090 km.
'''

class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 60
        self.matka = 2000

    def kiihdytys(self, muutos):
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

    def tiedot(self):
        print(f"Auton rekisteritunnus on {self.rekisteritunnus}, huippunopeus {self.huippunopeus} km/h, "
              f"tämänhetkinen nopeus {self.nopeus} km/h ja kuljettu matka {self.matka:.0f} km.")

auto_1 = Auto("ABC-123", 142)

#auto_1.tiedot()
auto_1.kiihdytys(0)
auto_1.kiihdytys(0)
auto_1.kiihdytys(0)
print(f"Auton nopeus on {auto_1.nopeus} km/h ja kuljettu matka on {auto_1.matka:.0f} km.")
auto_1.kulje(1.5)
print(f"Auton nopeus on {auto_1.nopeus} km/h ja kuljettu matka on {auto_1.matka:.0f} km.")
# print(f"Auton rekisteritunnus on {auto_1.rekisteritunnus}") tämä muistutuksena, miten printataan suoraan