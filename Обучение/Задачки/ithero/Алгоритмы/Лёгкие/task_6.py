"""
Совершенное число
Необходимо реализовать функцию is_perfect_number, которая на вход принимает число number и возвращает True,
если это число является совершенным, и False в противном случае.
"""

def is_perfect_number(number):
    sum = 0
    for i in range(1, number):
        if number % i == 0:
            sum += i
    return sum == number