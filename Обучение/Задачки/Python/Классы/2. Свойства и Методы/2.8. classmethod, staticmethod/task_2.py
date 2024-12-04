"""
Создайте класс Math с classmethod add, который принимает два числа и возвращает их сумму.
"""

class Math:
    @classmethod
    def addition(cls, n1, n2):
        return n1 + n2

    @staticmethod
    def subtraction(n1, n2):
        return n1 - n2

print('Метод класса - сложение чисел: ', Math.addition(1, 3))
print('Метод статический - вычитание чисел: ', Math.subtraction(1, 3))
