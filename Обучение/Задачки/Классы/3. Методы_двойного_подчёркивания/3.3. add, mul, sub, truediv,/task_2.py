# Класс определяет методы особым образом, результат которых не имеет какого-то особого смысла
class MyClass:
    def __init__(self, a, b=None):
        self.a = a

        if b is not None:
            self.b = b


    def __add__(self, other):
        print('Вызван метод __add__')
        return self.a + self.b + other

    def __mul__(self, other):
        print('Вызван метод __mul__')
        return self.a * self.b * other

    def __sub__(self, other):
        print('Вызван метод __mub__')
        return self.a - self.b - other

    def __truediv__(self, other):
        print('Вызван метод __truediv__')
        return self.a / self.b / other

# Тесты

a = MyClass(10,20)
print(a + 1, '\n') # 31
print(a.a, '\n') # (10) Атрибут a не изменился!
print(a * 2) # 400
print(a - 3) # -13
print(a / 4) # 0.125