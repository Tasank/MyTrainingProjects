import pytest
def human():
    name = 'Вася'
    return name

def human_age():
    age = 18
    return age

@pytest.mark.parametrize('name, age', [(human(), human_age())])
def test_human(name, age):
    assert str == type(name) and int == type(age)
    assert name == 'Вася'
    assert age >= 18