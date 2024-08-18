"""Классы животных"""

from random import choice
# Определения класса
class Dog:
    def __init__(self, age, name):
        # Атрибуты объекта
        self.age = age
        self.name = name
    # Метод класса
    def hungry(self):
        print(f'|{self.name}: Уаф! РРррр! Грр! Уав! Уаф! Оуу? Ууууу( ')

# Создание объектов класса
one_dog = Dog(3, 'Boby')
two_dog = Dog(2, 'Crazy')

print('|_____________________')
print('|   Проверка класса Dog.')

# Доступ к атрибутам
print(f'|Возраст собаки: {two_dog.age}')

# Вызов методов
two_dog.hungry()

print('|   Конец проверки    ')
print('|_____________________')
# Класс хищника, атрибуты возраст, название, место обитания и пол

class Predator:
    def __init__(self, age, name, habitat, gender):
        self.age = age
        self.name = name
        self.habitat = habitat
        self.gender = gender
    # Метод выводит информацию об объекте
    def info(self):
        print((f'Объект - {self.name}| возраст - {self.age}| место обитания - {self.habitat}| особь - ({self.gender})'
                f' пола.'))


# Множества для генерации случайных объектов
age_set = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11}
name_set = {'Кошка     ', 'Волк      ', 'Ястреб    ', 'Крокодил  ', 'Стервятник', 'Лев       ', 'Барс      ',
            'Леопард   '}
habitat_set = {'Московский зоопарк', 'Каньон', 'Тайга', 'Степь', 'Горы', 'Тундра', 'Тропики', 'Пустыня'}
gender_set = {'мужского', "женского"}

object_dict = {}

ask_count = int(input('Введите желаемое количество создания объектов(число): '))
for i in range(ask_count):
    age = choice(list(age_set))
    name = choice(list(name_set))
    habitat = choice(list(habitat_set))
    gender = choice(list(gender_set))


    predator = Predator(age, name, habitat, gender)
    predator.info()

    object_dict[f'predator_{i}'] = predator

print(f'Всего объектов: {len(object_dict)}')

# Для проверки содержимого словаря
for key, predator in object_dict.items():
    print(f'{key}: {predator.age}, {predator.habitat}, {predator.gender}')
