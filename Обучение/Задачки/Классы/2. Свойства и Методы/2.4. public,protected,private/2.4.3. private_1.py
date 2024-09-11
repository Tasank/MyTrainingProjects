"""
Демонстрация приватных атрибутов и методов.
Позволяют нам обратиться к ним только внутри класса.
Инициализация через (__) нижнее подчеркивание self.__атрибут
"""
class Triangle:
    def __init__(self, a, b, c):
        self.__a = a
        self.__b = b
        self.__c = c

    def perimeter(self):
        print('Периметр треугольника:', self.__a + self.__b + self.__c)
    def __private_perimeter(self):
        print('Периметр приватного треугольника:', self.__a + self.__b + self.__c)

t = Triangle(3,4,5)

t.perimeter() # Вывод Периметр треугольника: 12
t._Triangle__private_perimeter() # Вывод Периметр приватного треугольника: 12
print(t._Triangle__a) # Вывод 3
print(t._Triangle__b) # Вывод 4
print(t._Triangle__c) # Вывод 5

t.__private_perimeter() # Вывод AttributeError: 'Triangle' object has no attribute '__private_perimeter'
