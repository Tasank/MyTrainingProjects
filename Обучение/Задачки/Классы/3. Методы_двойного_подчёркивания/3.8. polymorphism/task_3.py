"""
Добавьте метод get_perimeter в классы Rectange, Square и Circle.
Реализуйте этот метод для каждого класса.
"""
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_perimeter(self):
        return 2 * (self.width + self.height)

class Square:
    def __init__(self, side):
        self.side = side

    def get_perimeter(self):
        return 4 * self.side

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def get_perimeter(self):
        return 2 * 3.14 * self.radius

r = Rectangle(5, 10)
s = Square(5)
c = Circle(10)

figure = [r, s, c]

for fig in figure:
    print(f'Периметр фигуры: {fig.get_perimeter():.2f}')
