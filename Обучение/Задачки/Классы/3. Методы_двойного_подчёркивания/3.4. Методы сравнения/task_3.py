"""
Определите класс Rectangle с атрибутами width и height, которые представляют собой ширину и высоту прямоугольника.
Переопределите методы __eq__ и __le__, чтобы определить, когда два прямоугольника равны и
когда один прямоугольник меньше или равен другому.

Например, если у вас есть два прямоугольника r1 = Rectangle(2, 3) и r2 = Rectangle(2, 3),
то r1 == r2 должно вернуть True, а r1 <= r2 должно вернуть True.
Если у вас есть два прямоугольника r1 = Rectangle(2, 3) и r2 = Rectangle(3, 4), то r1 <= r2 должно вернуть True.
"""


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    #
    @property
    def area(self):
        print('Площадь равна: ')
        return self.width * self.height

    def __eq__(self, other):
        # isinstance нужно для того чтобы проверить что other это прямоугольник
        if isinstance(other, Rectangle):
            print()
            return self.width == other.width and self.height == other.height
        # NotImplemented - это значение по умолчанию, если метод не переопределен
        return NotImplemented

    def __le__(self, other):
        if isinstance(other, Rectangle):
            print()
            return self.width <= other.width and self.height <= other.height
        return NotImplemented


r1 = Rectangle(4, 5)
print(r1.area)

r2 = Rectangle(10, 10)
print(r2.area)

print(r1 == r2)
print(r1 <= r2)