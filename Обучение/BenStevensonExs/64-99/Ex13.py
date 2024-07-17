"""
Упражнение 13. Размен.
Напишите программу, которая будет запрашивать у пользователя сумму сдачи в центах.
После этого она должна рассчитать и вывести на экран, сколько и каких монет потребуется для выдачи указанной суммы,
при условии что должно быть задействовано минимально возможное количество монет.
Допустим, у нас есть в распоряжении монеты достоинством в 1, 5, 10, 25 центов,
а также в 1 (loonie) и 2 (toonie) канадских доллара.
"""


def calculate_change(change_cent):
    # Номиналы монет в центах
    toonie = 200
    loonie = 100
    quarter = 25
    dime = 10
    nickel = 5
    penny = 1

    # Расчет количества монет
    num_toonies = change_cent // toonie
    change_cent %= toonie

    num_loonies = change_cent // loonie
    change_cent %= loonie

    num_quarters = change_cent // quarter
    change_cent %= quarter

    num_dimes = change_cent // dime
    change_cent %= dime

    num_nickels = change_cent // nickel
    change_cent %= nickel

    num_pennies = change_cent // penny

    return num_toonies, num_loonies, num_quarters, num_dimes, num_nickels, num_pennies


# Ввод суммы сдачи
change_cent = int(input('Введите сумму сдачи в центах: '))

# Получение количества монет каждого номинала
num_toonies, num_loonies, num_quarters, num_dimes, num_nickels, num_pennies = calculate_change(change_cent)


print('---Выдача монет для указанной суммы---')
print(f'Канадских долларов (2) - {num_toonies}')
print(f'Долларов (1)           - {num_loonies}')
print(f'(25)-Центовых монет    - {num_quarters}')
print(f'(10)-Центовых монет    - {num_dimes}')
print(f'(5)-Центовых монет     - {num_nickels}')
print(f'(1)-Центовых монет     - {num_pennies}')