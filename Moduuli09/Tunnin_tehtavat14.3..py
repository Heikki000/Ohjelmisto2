class Dog:       #luokka aloitetaan aina isolla kirjaimella
    def __init__(self, name, weight, age):
        print(f"Uusi koira luotu, nimi: {name}")
        self.name = name
        self.weight = weight
        self.age = age

    def say_hello(self):
        print(f"Hei, olen {self.name}, "
              f"paino: {self.weight} kg, ikä: {self.age} vuotta")
dog1 = Dog("Rekku", 5, 2)
dog2 = Dog("Ruffe", 8, 12)

dog1.say_hello()
dog2.say_hello()

