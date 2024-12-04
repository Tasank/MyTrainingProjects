"""
Определите класс Point с атрибутами x и y, которые представляют собой координаты точки на плоскости.
Переопределите методы __eq__ и __lt__, чтобы определить, когда две точки равны и когда одна точка находится ниже другой.

Например, если у вас есть две точки p1 = Point(1, 2) и p2 = Point(1, 2), то p1 == p2 должно вернуть True, \
а p1 < p2 должно вернуть False.
"""


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Переопределение (=)
    def __eq__(self, other):
        if isinstance(other, Point):
            return self.x == other.x and self.y == other.y

    # Переопределение (<)
    def __lt__(self, other):
        if isinstance(other, Point):
            return self.x < other.x and self.y < other.y


p1 = Point(1, 2)
p2 = Point(1, 2)
print(p1 == p2)
print(p1 < p2)
print(p1 > p2)
