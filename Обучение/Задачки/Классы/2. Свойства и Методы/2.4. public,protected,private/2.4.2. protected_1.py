"""
Демонстрация защищённых атрибутов и методов.
Позволяют нам обратиться к ним вне класса.
Инициализация через (_) нижнее подчеркивание self._атрибут
"""
class Triangle:
    def __init__(self, a, b, c):
        self._a = a
        self._b = b
        self._c = c

    def perimeter(self):
        print('Периметр треугольника:', self._a + self._b + self._c)

t = Triangle(3,4,5)
t.perimeter()
print(t._a)
print(t._b)
print(t._c)
