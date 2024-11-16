"""
Создайте класс `Point` с атрибутами `x` и `y`. Используйте `__slots__` для определения атрибутов класса.
Создайте объект класса `Point` и попробуйте изменить значение атрибута `x`.
"""

class Point:
    __slots__ = ('x', 'y')

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'({self.x}, {self.y})'


sec = Point(5, 10)
print(sec)

sec.x = 100
print(sec.x)
