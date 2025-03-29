import random

# Ввод имени игрока
name = input("Введи своё имя: ")

# Класс игрока
class Player:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage

# Класс врага
class Enemy:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage

# Функция для создания героя
def create_hero(name, race, prof):
    base_hp = 180
    base_dmg = 25
    hp = base_hp * races[race][0] * profs[prof][0]
    dmg = base_dmg * races[race][1] * profs[prof][1]
    return Player(name, hp, dmg)

# Словари характеристик рас и профессий
races = {
    "эльф": (1.5, 1),
    "гном": (0.8, 1.2),
    "человек": (1, 1)
}

profs = {
    "лучник": (0.9, 2),
    "щитоносец": (2, 0.6),
    "рыцарь": (1.2, 1.2)
}

# Выбор расы
race = ""
while race not in races:
    print(f"Выберите расу: {', '.join(races.keys())}")
    race = input("-> ").lower()

# Выбор профессии
prof = ""
while prof not in profs:
    print(f"Выберите профессию: {', '.join(profs.keys())}")
    prof = input("-> ").lower()

# Создание героя
hero = create_hero(name, race, prof)
print(f"Здравствуй, герой с именем {hero.name}!\n" 
      f"Твоё здоровье равно {hero.hp} HP.\n"
      f"Твой урон равен {hero.damage} единицам.\n" 
      f"Желаю удачи в приключениях, странник! 🏹🔪")

# Параметры врага
enemy_names = ["Орк", "Тролль", "Гоблин", "Дракон", "Скелет"]
enemy_hp_values = [100, 150, 200, 250, 300]
enemy_damage_values = [15, 20, 25, 30, 35]

# Функция для создания врага
def create_enemy():
    name = random.choice(enemy_names)
    hp = random.choice(enemy_hp_values)
    damage = random.choice(enemy_damage_values)
    return Enemy(name, hp, damage)

# Создание врага
enemy = create_enemy()
print(f"Враг появился! Это {enemy.name} с {enemy.hp} HP и {enemy.damage} урона!")
