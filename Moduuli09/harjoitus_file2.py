import random


class Auto:
    auto_count = 0

    def __init__(self, rekisteritunnus, huippunopeus):
        Auto.auto_count += 1
        print(f"{Auto.auto_count}. Uusi auto luotu, rekisteri: {rekisteritunnus} ja huippunopeus {huippunopeus}.")
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
        if self.matka < 1000:
            self.matka += aika * self.nopeus

    def tiedot(self):
        print(f"Auton rekisteritunnus on {self.rekisteritunnus}, huippunopeus {self.huippunopeus} km/h, "
              f"tämänhetkinen nopeus {self.nopeus} km/h ja kuljettu matka {self.matka:.0f} km.")


autot = [Auto("ABC-" + str(i + 1), random.randint(100, 200)) for i in range(10)]

for auto in autot:
    while auto.matka < 1000:
        auto.kiihdytä(random.randint(-10, 15))
        auto.kulje(1)
        auto.tiedot()
        if auto.matka >= 1000:
            print(f"Auto {auto.rekisteritunnus} on saavuttanut 1000 km:n matkan.")
            break
