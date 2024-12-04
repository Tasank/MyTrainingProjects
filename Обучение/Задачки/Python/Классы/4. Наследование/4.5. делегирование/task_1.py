"""
Создайте класс `Rectangle` с атрибутами `width` и `height`.
Создайте подкласс `Square` с атрибутом `side`.
Используйте делегирование для инициализации объектов класса `Square`.
"""

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def __str__(self):
        return f'Прямоугольник: ширина = {self.width}, высота = {self.height}'

class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)

    def __str__(self):
        return f'Квадрат: сторона = {self.width}'

square = Square(5)
print(square)
print(f'Площадь: {square.area()}')
print(f'Периметр: {square.perimeter()}')