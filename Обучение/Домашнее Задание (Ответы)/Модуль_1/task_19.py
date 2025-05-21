import random


class Enemy:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage


enemy_names = ["Орк", "Тролль", "Гоблин", "Дракон", "Скелет"]
enemy_hp_values = [100, 150, 200, 250, 300]
enemy_damage_values = [15, 20, 25, 30, 35]


def create_enemy():
    name = random.choice(enemy_names)
    hp = random.choice(enemy_hp_values)
    damage = random.choice(enemy_damage_values)
    enemy = Enemy(name, hp, damage)
    return enemy


enemy = create_enemy()
print(f"Враг появился! Это {enemy.name} с {enemy.hp} HP и {enemy.damage} урона!")
