import task_11

def calculate():
    a = int(input('Введите первое число: '))
    b = int(input('Введите второе число: '))
    operator = input('Введите оператор (+ или -): ')

    if operator == '+':
        print('Сумма:', task_11.summa(a, b))
    elif operator == '-':
        print('Разность:', task_11.raznost(a, b))
    else:
        print('\nНеправильный ввод! Попробуйте ещё раз.\n')
        calculate()

calculate()