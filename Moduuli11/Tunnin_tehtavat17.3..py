import random

class Animal:
    animal_count = 0
    def __init__(self, name, weight, age):
        Animal.animal_count += 1
        self.name = name
        self.weight = weight
        self.age = age
        self.energy_level = 500  # 0-1000
        self.distance = 0  # meters

    def eat(self):
        self.energy_level = 1000

    def run(self, meters):
        while meters > 0 and self.energy_level - 1 >= 0:
            meters -= 1
            self.distance = self.distance + 1
            self.energy_level = self.energy_level - 1

    def say_hello(self):
        print(f"paino: {self.weight} kg, ikä: {self.age} vuotta, "
              f"energiaa jäljellä {self.energy_level}, "
              f"juoksemani matka {self.distance} metriä")


class Predator():

    def attack(self):
        print("ATTACKING!!!")


class Dog(Animal):
    def __init__(self, name, weight, age):
        super().__init__(name, weight, age)

    def say_hello(self):
        print(f"Wuf, olen {self.name}-niminen koira.")
        super().say_hello()

class Cat(Animal):
    def __init__(self, name, weight, age):
        super().__init__(name, weight, age)

    def say_hello(self):
        print(f"Miau, olen {self.name}-niminen kissa")
        super().say_hello()

class Wolf(Animal, Predator):
    def __init__(self, name, weight, age):
        Animal.__init__(self, name, weight, age)


dog1 = Dog("Ruffe", 8, 10)
cat1 = Cat("Mirri", 5, 15)

animals = [dog1, cat1]
for a in animals:
    a.eat()
    a.run(random.randint(10, 500))
    a.say_hello()

print(f"Eläinolioita luotu yhteensä: {Animal.animal_count}")

wolf = Wolf("Sus", 10, 8)
wolf.say_hello()
wolf.attack()