class Vehicle:
    def __init__(self, speed=0):
        self.speed = speed
    def accelerate(self, increment):
        self.speed += increment / 2

class Car(Vehicle):
    def __init__(self, speed=0, fuel=100):
        super().__init__(speed)
        self.fuel = fuel
    def accelerate(self, increment):
        super().accelerate(increment * 2)
        self.fuel -= increment / 2

my_sedan = Car()
my_pickup = Vehicle()

my_sedan.accelerate(20)
my_pickup.accelerate(20)

print("Седан едущий со скоростью {} км/ч с топливом {:.0f}%".format(my_sedan.speed, my_sedan.fuel))
print("Пикап едущий со скоростью {} км/ч".format(my_pickup.speed))