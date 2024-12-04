"""
4. Создайте класс `Calculator` с staticmethod `calculate`, который принимает выражение и возвращает его результат.

"""
class Calculator:
    @staticmethod
    def calculate_1(expr):
        # eval это функция для вычисления выражения, которая может:
        # вычислять выражения, вычислять математические функции, вычислять логические функции и т.д.
        return eval(expr)

print(Calculator.calculate_1("2+2-4/2"))
