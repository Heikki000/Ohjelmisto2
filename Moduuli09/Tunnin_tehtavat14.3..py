class Dog:       #luokka aloitetaan aina isolla kirjaimella
    def __init__(self, name, weight, age):
        print(f"Uusi koira luotu, nimi: {name}")
        self.name = name
        self.weight = weight
        self.age = age
        self.energyLevel = 50   # 0-100
        self.distance = 0   # meters

    def eat(self):
        self.energyLevel = 100

    def run(self, meters):
        while self.energyLevel - meters * 0.1 >= 0:
            self.distance = self.distance + meters
            self.energyLevel = self.energyLevel - meters * 0.1

    def say_hello(self):
        print(f"Hei, olen {self.name}, "
              f"paino: {self.weight} kg, ikä: {self.age} vuotta,"
              f"energiaa jäljellä {self.energyLevel}, "
              f"juoksemani matka {self.distance} metriä.")


dog1 = Dog("Rekku", 5, 2)
dog2 = Dog("Ruffe", 8, 12)
dog1.eat()
dog1.run(1000)
dog2.run(2000)
dog1.say_hello()
dog2.say_hello()

