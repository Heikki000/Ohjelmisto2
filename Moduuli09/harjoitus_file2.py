import random
from time import sleep
class Auto:
    def _init_(self, rekisteritunnus, huippunopeus):
        self.register = rekisteritunnus
        self.topspeed = huippunopeus
        self.speed = 0
        self.traveled = 0

    def acceleration(self, speed):

        self.speed += speed

        if self.speed >= self.topspeed:
            self.speed = self.topspeed
        elif self.speed < 0:
            self.speed = 0

    def travel(self, hour):
        self.traveled += self.speed * hour


    pass

cars = []
for n in range(1, 11):
    car = Auto("ABC-"+str(n), random.randint(100,200))
    cars.append(car)

game= True
while game == True:
    for car in cars:
        if car.traveled > 10000:
            game = False
            break
        else:
            car.acceleration(random.randint(-10,15))
            car.travel(1)


for car in cars:
    print(f"|{car.register:^{10}}|{car.topspeed:^{10}}|{car.speed:^{10}}|{car.traveled:^{10}}|")