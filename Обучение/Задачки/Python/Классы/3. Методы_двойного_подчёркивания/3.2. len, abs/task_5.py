"""
__abs__
Класс "Комплексное число": Создайте класс MyComplex, который хранит комплексное число и имеет метод __abs__,
который возвращает абсолютное значение комплексного числа.

Класс "Вектор": Создайте класс MyVector, который хранит вектор в n-мерном пространстве и имеет метод __abs__,
который возвращает длину вектора.
"""
from math import sqrt
class MyComplex:
    def __init__(self, real=0, imag=0):
        self.real = real
        self.imag = imag
    #  формула |a + bi| = sqrt(a^2 + b^2)
    def __abs__(self):
        return sqrt(self.real**2 + self.imag**2)

    def __str__(self):
        return (f'Комплексное число: {self.real} + {self.imag}i\n'
                f'Абсолютное значение: {abs(self)}')

my_complex = MyComplex(3, 4)
print(my_complex)
print()

class MyVector:
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z
    def __abs__(self):
        return sqrt(self.x**2 + self.y**2 + self.z**2)

    def __str__(self):
        return (f'Вектор: {self.x} + {self.y} + {self.z}\n'
                f'Длина вектора: {abs(self)}')

my_vector = MyVector(3, 4, 5)
print(my_vector)