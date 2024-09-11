"""
Демонстрация публичных атрибутов и методов.
"""
class Triangle:
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c

    def perimeter(self):
        print('Периметр треугольника:', self.a + self.b + self.c)

t = Triangle(3,4,5)
t.perimeter()
print(t.a, t.b, t.c)
