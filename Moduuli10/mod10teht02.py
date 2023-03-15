'''
Jatka edellisen tehtävän ohjelmaa siten, että teet Talo-luokan.
Talon alustajaparametreina annetaan alimman ja ylimmän kerroksen numero sekä hissien lukumäärä.
Talon luonnin yhteydessä talo luo tarvittavan määrän hissejä. Hissien lista tallennetaan
talon ominaisuutena. Kirjoita taloon metodi aja_hissiä, joka saa parametreinaan hissin numeron ja kohdekerroksen.
Kirjoita pääohjelmaan lauseet talon luomiseksi ja talon hisseillä ajelemiseksi.
'''

class Hissi:
    def __init__(self, alin, ylin):
        self.alin = alin
        self.ylin = ylin
        self.kerros = 0

    def kerros_ylös(self):
        self.kerros += 1
        print(f"Hissi on kerroksessa {self.kerros}.")
        return

    def kerros_alas(self):
        self.kerros -= 1
        print(f"Hissi on kerroksessa {self.kerros}.")
        return

    def siirry_kerrokseen(self, uusi_kerros):
        while self.kerros < uusi_kerros:
            self.kerros_ylös()
        while self.kerros > uusi_kerros:
            self.kerros_alas()
        if self.kerros == uusi_kerros:
            print(f"Olet heluamassasi kerroksessa, kerros {uusi_kerros:.0f}:ssa!")
            return

class Talo:
    def __init__(self, alin, ylin, hissien_lkm):
        self.alin = alin
        self.ylin = ylin
        self.hissit = [Hissi(alin, ylin) for n in range(hissien_lkm)]

    def aja_hissiä(self, hissi_nro, kohde_kerros):
        hissi = self.hissit[hissi_nro - 1]
        if kohde_kerros < self.alin or kohde_kerros > self.ylin:
            print("Virhe: kohdekerros on talon ulkopuolella.")
            return
        hissi.siirry_kerrokseen(kohde_kerros)

kohde = 0
talo = Talo(1, 7, 3)
print("Tervetuloa käyttämään talon hissejä. Olet nyt talon alimmassa eli 1. kerroksessa.")
while kohde != '':
    kohde = int(input("Mihin kerrokseen haluat mennä (1-7)? "))
    while kohde < 1 or kohde > 7:
        print("Virhe: kerros on talon ulkopuolella.")
        kohde = int(input("Mihin kerrokseen haluat mennä (1-7)? "))
    hissi_nro = int(input(f"Minkä hissin haluat ottaa (1-{len(talo.hissit)})? "))
    talo.aja_hissiä(hissi_nro, kohde)



