"""
Задание: Создайте класс Car с calculated property speed_in_kmh,
которое вычисляет скорость автомобиля в километрах в час на основе скорости в милях в час.

Требования:

Класс Car должен иметь метод set_speed_in_mph(speed), который устанавливает скорость автомобиля в милях в час.
Calculated property speed_in_kmh должно вычислять скорость автомобиля в километрах в час,
используя коэффициент пересчета 1 миля = 1,60934 километра.
Создайте экземпляр класса Car и установите скорость в милях в час.
Выведите скорость автомобиля в километрах в час.
"""

class Car:
    def __init__(self):
        self.speed = 0
    @property
    def speed_in_mph(self):
        print(f'Текущая скорость: {self.speed} миль в час')
        return self.speed
    @speed_in_mph.setter
    def speed_in_mph(self, speed):
        print(f'Установлена скорость: {speed} миль в час')
        self.speed = speed

    # вычисляемое свойство
    @property
    def speed_in_kmh(self):
        return self.speed * 1.60934

my_car = Car()
my_car.speed_in_mph = 100
print(f'Скорость в километрах в час: {my_car.speed_in_kmh}')
