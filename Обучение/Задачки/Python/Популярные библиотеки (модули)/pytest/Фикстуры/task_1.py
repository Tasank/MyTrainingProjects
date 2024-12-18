import pytest


@pytest.fixture
def func():
    a = 1
    b = 2
    return a, b

def test_num(func):
    assert int == type(func[0]) and int == type(func[1])
    assert func[0] + func[1] == 3
