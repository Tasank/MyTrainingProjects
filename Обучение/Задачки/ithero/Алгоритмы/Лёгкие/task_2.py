"""
Необходимо реализовать функцию get_numbers_divisible_by_7_not_by_5,
которая на вход принимает два числа start и end и возвращает список всех чисел,
включая граничные числа start и end, которые делятся на 7, но не делятся на 5.

Пример

start = 10
end = 38
numbers = get_numbers_divisible_by_7_not_by_5(start, end)
print(numbers)
# Ожидаемый вывод: [14, 21, 28]
"""

def get_numbers_divisible_by_7_not_by_5(start, end):
    return[i for i in range(start, end +1) if i % 7 ==0 and i % 5 != 0]



start = 10
end = 38
numbers = get_numbers_divisible_by_7_not_by_5(start, end)
print(numbers)