"""
Создайте класс Triangle, который наследует от класса Figure.
Реализуйте метод get_area для класса Triangle.
"""
class Figure:
    def __init__(self):
        pass

    def get_area(self):
        raise NotImplementedError(f'метод get_area не реализован в классе {self.__class__.__name__}')


class Triangle(Figure):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def get_area(self):
        p = (self.a + self.b + self.c) / 2
        return (p * (p - self.a) * (p - self.b) * (p - self.c)) ** 0.5

# a = Figure()
# print(a.get_area())

t = Triangle(3, 4, 5)
print(f'Площадь треугольника: {t.get_area():.2f}')
