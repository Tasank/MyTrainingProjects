class Calculator:
    def __init__(self):
        self.history = []

    def __call__(self, a, operator, b):
        global result
        try:
            if operator == '+':
                result = a + b
            elif operator == '-':
                result = a - b
            elif operator == '*':
                result = a * b
            elif operator == '/':
                try:
                    result = a / b
                except ZeroDivisionError:
                    print(f'Ошибка: деление на ноль ')
            else:
                raise ValueError("Ошибка: недопустимая операция")
        except:
            print('---Ошибка---')

        self.history.append((a, operator, b, result))
        print(f'{a} {operator} {b} = {result}')

        result = 0


cal = Calculator()

cal(1, '+', 2)  # 1 + 2 = 3
cal(2, '-', 2)  # 2 - 2 = 0
cal(5, "/", 0)  # Ошибка: деление на ноль (\n\n) 5 / 0 = 0
cal('2', '*', 2)  # 2 * 2 = 22
cal('wda', '*', 'ad')
