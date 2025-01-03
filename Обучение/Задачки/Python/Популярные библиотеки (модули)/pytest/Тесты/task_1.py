"""
Написать тест для функции sum_two, которая принимает двt переменные и возвращает их сумму.
"""
import pytest
a = '1'
b = 2
def sum_two(a, b):
    return a + b
def test_sum():
    assert sum_two(1, 2) == 3

def test_type():
    assert int == type(sum_two(a, b))

