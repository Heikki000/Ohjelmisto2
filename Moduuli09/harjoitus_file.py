import random

autot = []

class Auto:
    auto_count = 0
    def __init__(self, rekisteritunnus, huippunopeus):
        Auto.auto_count += 1
        print(f"{Auto.auto_count}. Uusi auto luotu, rekisteri: {rekisteritunnus} ja huippunopeus {huippunopeus}.")
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.matka = 0

for i in range(10):
    autot.append(Auto("ABC-" + str(i+1), random.randint(100,200)))

print(autot[4])
print(random.randint(100,102))