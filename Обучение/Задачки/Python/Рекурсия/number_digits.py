"""
Напишите рекурсивную функцию, которая будет принимать на вход целое число и возвращать количество цифр в этом числе.
"""

def number_count(number):
    if number < 10:
        return 1
    return 1 + number_count(number // 10)

print(number_count(100))