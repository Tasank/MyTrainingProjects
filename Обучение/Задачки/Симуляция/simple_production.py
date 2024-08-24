"""
Это симуляция максимально простого взаимодействия производства с использованием времени
"""
from random import choice
def deposit(count):
    name_set = ['Уголь', "Камень", "дерево", "Песок"]
    return count, choice(name_set)

## Описать класс фабрики
class Fabric:


def player(time):
    # 1 ресурс в 1 минуту
    mining_speed = 1
    extracted_resource = 0
    n = 1

    count, name_deposit = deposit(1000)

    while time != 0 and count > 0:
        extracted_resource += mining_speed

        if extracted_resource == 50:
            extracted_resource = 0
            ## Прописать создание объекта Фабрики



    return mining_speed * time

## Прописать основную функцию
def play():
    time = int(input('Введите количество минут симуляции: '))
