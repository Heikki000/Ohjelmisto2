class Dog:       #luokka aloitetaan aina isolla kirjaimella

    dog_count = 0

    def __init__(self, name, weight, age):
        Dog.dog_count += 1
        print(f"{Dog.dog_count}. Uusi koira luotu, nimi {name}")
        print(f"Uusi koira luotu, nimi: {name}")
        self.name = name
        self.weight = weight
        self.age = age
        self.energy_level = 500   # 0-100
        self.distance = 0   # meters

    def eat(self):
        self.energy_level = 1000

    def run(self, meters):
        while meters > 0 and self.energy_level - 1 >= 0:
            meters -= 1
            self.distance = self.distance + 1
            self.energy_level = self.energy_level - 1

    def say_hello(self):
        print(f"Hei, olen {self.name}, "
              f"paino: {self.weight} kg, ikä: {self.age} vuotta,"
              f"energiaa jäljellä {self.energy_level:.0f}, "
              f"juoksemani matka {self.distance} metriä.")


dog1 = Dog("Rekku", 5, 2)
dog2 = Dog("Ruffe", 8, 12)
dog1.eat()
dog1.run(1000)
dog2.run(2000)
dog1.say_hello()
dog2.say_hello()

dog3 = Dog("Muro", 12, 10)

print(f"Koiria luotu yhteensä: {Dog.dog_count}")
