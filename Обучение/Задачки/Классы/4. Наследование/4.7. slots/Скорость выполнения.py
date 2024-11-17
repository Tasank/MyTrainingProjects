"""
Разница скорости выполнения. Демонстрация создания 1 000 000 объектов
и выполнения действий.
"""

from timeit import timeit
from random import randint

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class PersonSlots:
    __slots__ = ['name', 'age']

    def __init__(self, name, age):
        self.name = name
        self.age = age

def create_obj_person():
    return [Person(f'Человек {i}', i) for i in range(1000000)]

def create_obj_personslots():
    return [PersonSlots(f'Человек {i}', i) for i in range(1000000)]

def update_obj_person(persons):
    for person in persons:
        person.name = f'Человек №{person.age}'
        person.age += randint(0, 10)
        if person.age % 2 == 0:
            del person.age
        del person.name

def update_obj_personslots(persons):
    for person in persons:
        person.name = f'Человек №{person.age}'
        person.age += randint(0, 10)
        if person.age % 2 == 0:
            del person.age
        del person.name

print(f'Скорость создания объектов Person: {timeit(create_obj_person, number=1)}')
print(f'Скорость создания объектов PersonSlots: {timeit(create_obj_personslots, number=1)}')

persons = create_obj_person()
personslots = create_obj_personslots()
print()

print(f'Скорость изменения объектов Person: {timeit(lambda: update_obj_person(persons), number=1)}')
print(f'Скорость изменения объектов PersonSlots: {timeit(lambda: update_obj_personslots(personslots), number=1)}')

# Тесты

"""
___________________________________

Скорость создания объектов Person: 2.397739800158888
Скорость создания объектов PersonSlots: 1.8958385000005364

Скорость изменения объектов Person: 4.308362999930978
Скорость изменения объектов PersonSlots: 4.367012199945748
____________________________________

Скорость создания объектов Person: 4.88117800001055
Скорость создания объектов PersonSlots: 2.4383398999925703

Скорость изменения объектов Person: 5.765627800021321
Скорость изменения объектов PersonSlots: 4.4303572999779135
____________________________________

Скорость создания объектов Person: 4.02060310007073
Скорость создания объектов PersonSlots: 2.998222199967131

Скорость изменения объектов Person: 4.4387978001032025
Скорость изменения объектов PersonSlots: 4.397538400022313
____________________________________
"""

