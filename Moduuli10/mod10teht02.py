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
        self.kerros = 1

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
            print(f"Hissi on haluamassasi kerroksessa, kerros {uusi_kerros:.0f}:ssa!\n")
            return

class Talo:
    def __init__(self, alin, ylin, hissien_lkm):
        self.alin = alin
        self.ylin = ylin
        self.hissien_lkm = hissien_lkm
        self.hissit = []
        for n in range(hissien_lkm):
            self.hissit.append(Hissi(alin, ylin))

    def aja_hissiä(self, hissi_nro, uusi_kerros):
        self.hissi_nro = self.hissit[-1]
        self.hissit[hissi_nro].siirry_kerrokseen(uusi_kerros)


uusi_kerros = 0
talo = Talo(1, 7, 3)
print("Tervetuloa ajelemaan talon hissejä. Olet nyt talon alimmassa eli 1. kerroksessa.")

hissi_nro = int(input(f"Minkä hissin haluat valita (1-{len(talo.hissit)})? "))
while hissi_nro < 1 or hissi_nro > len(talo.hissit):
    print("Virhe: Valitsit virheellisen hissinumeron, yritä uudelleen.")
    hissi_nro = int(input(f"Minkä hissin haluat valita (1-{len(talo.hissit)})? "))
while hissi_nro != '':
    hissi_nro = int(hissi_nro) - 1
    uusi_kerros = int(input("Mihin kerrokseen haluat lähettää hissin (1-7)? "))
    while uusi_kerros < 1 or uusi_kerros > 7:
            print("Virhe: kerros on talon ulkopuolella.")
            uusi_kerros = int(input("Mihin kerrokseen haluat lähettää hissin (1-7)? "))
    talo.aja_hissiä(hissi_nro, uusi_kerros)
    hissi_nro = input(f"Minkä hissin haluat valita (1-{len(talo.hissit)})? (tai paina ENTER lopettaaksesi) ")
    if hissi_nro == '':
        break


print("Ohjelma lopetettu")




