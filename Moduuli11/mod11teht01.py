'''
Toteuta seuraava luokkahierarkia Python-kielellä: Julkaisu voi olla kirja tai lehti.
Jokaisella julkaisulla on nimi. Kirjalla on lisäksi kirjoittaja ja sivumäärä, kun taas lehdellä on päätoimittaja.
Kirjoita luokkiin myös tarvittavat alustajat. Tee aliluokkiin metodi tulosta_tiedot,
joka tudostaa kyseisen julkaisun kaikki tiedot. Luo pääohjelmassa julkaisut Aku Ankka (päätoimittaja Aki Hyyppä)
ja Hytti n:o 6 (kirjailija Rosa Liksom, 200 sivua). Tulosta molempien julkaisujen kaikki tiedot toteuttamiesi metodien avulla.
'''

class Julkaisu:
    def __init__(self, nimi):
        self.nimi = nimi

class Kirja(Julkaisu):
    def __init__(self, nimi, kirjoittaja, sivumäärä):
        self.kirjoittaja = kirjoittaja
        self.sivumäärä = sivumäärä
        super().__init__(nimi)

    def tulosta_tiedot(self):
        print(f"Kirjan nimi on {self.nimi}.")
        print(f"Kirjan on kirjoittanut {self.kirjoittaja} ja siinä on {self.sivumäärä} sivua.")
        return

class Lehti(Julkaisu):
    def __init__(self, nimi, päätoimittaja):
        self.päätoimittaja = päätoimittaja
        super().__init__(nimi)

    def tulosta_tiedot(self):
        print(f"Lehden nimi on {self.nimi}.")
        print(f"Lehden päätoimittaja on {self.päätoimittaja}.")

lehti1 = Lehti('Aku Ankka', 'Aki Hyyppä')
kirja1 = Kirja('Hytti n:o 6', 'Rosa Liksom', 200)

julkaisut = [lehti1, kirja1]
print()
for j in julkaisut:
    j.tulosta_tiedot()
    print()