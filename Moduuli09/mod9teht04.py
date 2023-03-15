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

autot = []
matka = 0
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
        if self.matka < 10000:
            self.matka = self.matka + aika * self.nopeus
            return self.matka
        else:
            return


    def tiedot(self):
        print(f"Auton rekisteritunnus on {self.rekisteritunnus}, huippunopeus {self.huippunopeus} km/h, "
              f"tämänhetkinen nopeus {self.nopeus} km/h ja kuljettu matka {self.matka:.0f} km.")


for i in range(10):
    autot.append(Auto("ABC-" + str(i+1), random.randint(100,200)))

for auto in autot:
    if auto.matka >= 10000:
        print(f"Auto {auto.rekisteritunnus} on saavuttanut 1000 km:n matkan.")
        break
    else:
        while auto.matka < 10000:
            auto.kiihdytä(random.randint(-10, 15))
            auto.kulje(1)
            auto.tiedot()
            if auto.matka >= 10000:
                break


#print(autot)


