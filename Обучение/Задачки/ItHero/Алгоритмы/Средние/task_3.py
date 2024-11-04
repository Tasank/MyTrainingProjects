"""
Ugly number
Вам дано число n. Напишите функцию nthUglyNumber(n), которая вернет число - n-ное ugly number.

Примечание: ugly number - это положительное целое число, множители которого ограничены набором 2, 3 и 5.
Пример 1:

nthUglyNumber(10)

Результат: 12

Объяснение: [1, 2, 3, 4, 5, 6, 8, 9, 10, 12] - это первые 10 ugly numbers.

Пример 2:

nthUglyNumber(1)

Результат: 1

Объяснение: 1 также считается ugly number.
"""
def nthUglyNumber(n: int) -> int:
    ugly_numbers = [0] * n  # Массив для хранения первых n ugly numbers
    ugly_numbers[0] = 1  # Первое ugly number — это 1

    i2 = i3 = i5 = 0  # Указатели для множителей 2, 3 и 5

    next_multiple_of_2 = 2
    next_multiple_of_3 = 3
    next_multiple_of_5 = 5

    for i in range(1, n):
        # Выбираем минимальное из предложенных чисел
        ugly_numbers[i] = min(next_multiple_of_2, next_multiple_of_3, next_multiple_of_5)

        # Обновляем указатели и значения следующего множителя
        if ugly_numbers[i] == next_multiple_of_2:
            i2 += 1
            next_multiple_of_2 = ugly_numbers[i2] * 2

        if ugly_numbers[i] == next_multiple_of_3:
            i3 += 1
            next_multiple_of_3 = ugly_numbers[i3] * 3

        if ugly_numbers[i] == next_multiple_of_5:
            i5 += 1
            next_multiple_of_5 = ugly_numbers[i5] * 5

    return ugly_numbers[-1]


print(nthUglyNumber(10))  # Вывод: 12
print(nthUglyNumber(1))   # Вывод: 1
