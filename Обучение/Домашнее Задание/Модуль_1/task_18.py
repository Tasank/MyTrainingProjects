# Практика урока

trip = {
    13: ("Гостиный двор", "ГДК", "Магазин Гипер", "Галерея"),
    25: ("Парк Победы", "Улица Ленина", "Главная площадь", "Речное депо")
}


class Bus:
    def __init__(self, trip):
        self.trip = trip

    def navigator(self, stop):
        line = trip[self.trip]
        print(f"Автобус {self.trip} прибыл на остановку {line[stop]}")


go = Bus(13)
for num in range(4):
   go.navigator(num)

print('\n\n----------------------------------------------\n\n')






# Домашнее задание
class Hero:
    def __init__(self,name, health, damage, armor):
        self.name = name
        self.health = health
        self.damage = damage
        self.armor = armor

    def battle_cry(self):
        print('ТЫ ПОПЛАТИШСЯ ЗА СОВЕРШЁННЫЕ ЗЛОДЕЯНИЯ!')


Gideon = Hero('Гидеон', 100, 10, 5)

print(f'Имя: {Gideon.name} \n'
      f'Здоровье: {Gideon.health} \n'
      f'Урон: {Gideon.damage} \n'
      f'Броня: {Gideon.armor}\n')

Gideon.battle_cry()