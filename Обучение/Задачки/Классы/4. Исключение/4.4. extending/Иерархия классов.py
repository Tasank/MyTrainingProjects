"""
Создайте иерархию классов для описания различных типов транспортных средств.
Класс Vehicle должен быть базовым классом,
а классы Car, Truck, Motorcycle и Bicycle должны быть подклассами класса Vehicle.
Каждый подкласс должен иметь свои уникальные методы и атрибуты.

Например, класс Car может иметь метод drive(), который печатает "Машина едет",
а класс Motorcycle может иметь метод ride(), который печатает "Мотоцикл едет".
"""

class Vehicle:
    def __init__(self, brand, max_speed):
        self.brand = brand
        self.max_speed = max_speed

class Car(Vehicle):
    def __init__(self, capacity, brand, max_speed):
        super().__init__(brand, max_speed)
        self.capacity = capacity

    def drive(self):
        print('Машина едет')

class Truck(Vehicle):
    def __init__(self, load_capacity, brand, max_speed):
        super().__init__(brand, max_speed)
        if isinstance(load_capacity, int):
            if 1 >= load_capacity >= 0.5:
                self.load_capacity = 'Малая грузоподъемность'
            elif 5 >= load_capacity >= 2:
                self.load_capacity = 'Средняя грузоподъемность'
            elif 16 >= load_capacity > 5:
                self.load_capacity = 'Большая грузоподъемность'
            elif load_capacity > 16:
                self.load_capacity = 'Особо большая грузоподъемность'
            else:
                self.load_capacity = 'Нет грузоподъемности'
        else:
            self.load_capacity = 'Нет грузоподъемности'

class Motorcycle(Vehicle):
    def ride(self):
        print('Мотоцикл едет')

class Bicycle(Vehicle):
    def ride(self):
        print('Велосипед едет')


car = Car(5, 'BMW', 250)
print(car.capacity)
print(car.brand)
print(car.max_speed)
car.drive()

print()

truck = Truck(16, 'Volvo', 200)
print(truck.brand)
print(truck.max_speed)
print(truck.load_capacity)

