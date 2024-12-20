"""
pytest.mark.parametrize
Проверка входных данных на тип данных
"""
import pytest

@pytest.mark.parametrize('a, b, c', [(1, '1', True,), (1, '', False), (2, 'data', True)])
def test_data(a, b, c):
    assert int == type(a) and str == type(b) and bool == type(c)

