'''
Nyt ohjelmoidaan autokilpailu. Uuden auton kuljettu matka alustetaan automaattisesti nollaksi.
Tee pääohjelman alussa lista, joka koostuu kymmenestä toistorakenteella luodusta auto-oliosta.
Jokaisen auton huippunopeus arvotaan 100 km/h ja 200 km/h väliltä. Rekisteritunnus luodaan seuraavasti
"ABC-1", "ABC-2" jne. Sitten kilpailu alkaa. Kilpailun aikana tehdään tunnin välein seuraavat toimenpiteet:

Jokaisen auton nopeutta muutetaan siten, että nopeuden muutos arvotaan väliltä -10 ja +15 km/h väliltä.
Tämä tehdään kutsumalla kiihdytä-metodia.
Kaikkia autoja käsketään liikkumaan yhden tunnin ajan. Tämä tehdään kutsumalla kulje-metodia.
Kilpailu jatkuu, kunnes jokin autoista on edennyt vähintään 10000 kilometriä.
Lopuksi tulostetaan kunkin auton kaikki ominaisuudet selkeäksi taulukoksi muotoiltuna.
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

autot = []

for i in range(10):
    autot.append(Auto("ABC-" + str(i+1), random.randint(100,200)))

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
    print(f"|{auto.rekisteritunnus:^{15}}|{auto.huippunopeus:^{15}}|{auto.nopeus:^{15}}|{auto.matka:^{15}}|")




