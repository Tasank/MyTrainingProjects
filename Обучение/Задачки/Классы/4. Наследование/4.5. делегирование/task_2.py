"""
Создайте класс Vehicle с атрибутами speed и color. Создайте подкласс Car с атрибутом engine.
Используйте делегирование для инициализации объектов класса Car.
Реализуйте методы сравнения объектов класса Car.
"""

class Vehicle:
    def __init__(self, speed, color):
        self.speed = speed
        self.color = color


class Car(Vehicle):
    def __init__(self, speed, color, engine):
        super().__init__(speed, color)
        self.engine = engine

    def __str__(self):
        return f"Скорость: {self.speed}, цвет: {self.color}, Двигатель: {self.engine}"


car1 = Car(100, 'red', 'бензиновый')
print(car1)
