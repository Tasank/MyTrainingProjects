"""
Создайте класс Person с атрибутами name и age. Используйте __slots__ для определения атрибутов класса.
Создайте объект класса Person и попробуйте добавить новый атрибут.
"""
class Person:
    __slots__ = ['name', 'age']

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f'Имя: {self.name} \nВозраст: {self.age}'


person = Person('Вася', 25)
print(person)

try:
    person.job = 'Инженер'
except AttributeError:
    print('Нельзя добавить новый атрибут')