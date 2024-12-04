"""
Напишите декоратор @property,
который принимает на вход функцию и возвращает функцию с помощью которой можно вычислить значение свойства.
"""
class Addition:
    def __init__(self, a, b):
        self._a = a
        self._b = b
    @property
    def sum(self):
        return self._a + self._b
    # Установить значение для a и b
    @sum.setter
    def sum(self, value):
        self._a = value
        self._b = value

a = Addition(1, 2)
print(a.sum)
a.sum = 10
print(a.sum)
