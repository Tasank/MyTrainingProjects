class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    @property
    def sum(self):
        return self.num1 + self.num2

    @sum.setter
    def sum(self, value):
        self.num1 = value[0]
        self.num2 = value[1]
        print(f'Результат сложения: {self.num1 + self.num2}')

    @property
    def sub(self):
        return self.num1 - self.num2

    @property
    def div(self):
        return self.num1 / self.num2

    @property
    def mul(self):
        return self.num1 * self.num2


a = Calculator(1, 5)
print(f'Сумма: {a.sum}')
x, y = float(input('Укажите первое число: ')), float(input('Укажите второе число: '))
a.sum = [x, y]
print(f'Вычитание: {a.sub}')
print(f'Деление: {a.div}')
print(f'Умножение: {a.mul}')
