class Hissi:
    def __init__(self, alin, ylin):
        self.alin = alin
        self.ylin = ylin
        self.kerros = 1

    def kerros_ylös(self):
        self.kerros += 1
        print(f"Hissi on kerroksessa {self.kerros}.")

    def kerros_alas(self):
        self.kerros -= 1
        print(f"Hissi on kerroksessa {self.kerros}.")

    def siirry_kerrokseen(self, uusi_kerros):
        while self.kerros < uusi_kerros:
            self.kerros_ylös()
        while self.kerros > uusi_kerros:
            self.kerros_alas()
        if self.kerros == uusi_kerros:
            print(f"Hissi on kerroksessa {self.kerros}.")


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


talo = Talo(1, 7, 2)
print("Tervetuloa hissiin! Olet nyt talon alimmassa eli 1. kerroksessa.")

while True:
    try:
        kohde = int(input("Mihin kerrokseen haluat mennä (1-7)? "))
    except ValueError:
        print("Virhe: syötä kokonaisluku.")
        continue
    if kohde < 1 or kohde > 7:
        print("Virhe: kerros on talon ulkopuolella.")
        continue
    hissi_nro = int(input(f"Mikä hissi haluat ottaa (1-{len(talo.hissit)})? "))
    talo.aja_hissiä(hissi_nro, kohde)
