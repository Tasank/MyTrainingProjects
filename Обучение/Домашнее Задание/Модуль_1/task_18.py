class Hero:
    def __init__(self,name, health, damage, armor):
        self.name = name
        self.health = health
        self.damage = damage
        self.armor = armor

    def battle_cry(self):
        print('ТЫ ПОПЛАТИШСЯ ЗА СОВЕРШЁННЫЕ ЗЛОДЕЯНИЯ!')


Gideon = Hero('Гидион', 100, 10, 5)

print(f'Имя: {Gideon.name} \n'
      f'Здоровье: {Gideon.health} \n'
      f'Урон: {Gideon.damage} \n'
      f'Броня: {Gideon.armor}\n')

Gideon.battle_cry()