import random
import time

# Ввод имени игрока
name = input("Введи своё имя: ")

# Класс игрока
class Player:
    def __init__(self, name, hp, damage, xp=0, lvl=0):
        self.name = name
        self.hp = hp
        self.damage = damage
        self.xp = xp
        self.lvl = lvl

    def attack(self, victim):
        victim.hp -= self.damage
        print(f"Ты нанёс врагу {self.damage} урона. Теперь у него {victim.hp} здоровья.")
        # возврат состояния, чтобы игра понимала, когда и кто выигрывает\проигрывает
        if victim.hp <= 0:
            print(f"{victim.name} повержен!")
            return False
        else:
            return True




# Класс врага
class Enemy:
    races = {
        "Слизняк": (10, 10),
        "Волк": (25, 20),
        "Орк": (50, 45),
        "Группа гоблинов": (120, 25),
        "Оборотень": (150, 50),
        "Великан": (200, 100),
        "Дракон": (300, 200),
        "Скелет": (50, 10),

    }

    def __init__(self):
        self.name = random.choice(list(self.races.keys()))
        self.hp = self.races[self.name][0]
        self.damage = self.races[self.name][1]
        self.xp = self.hp * 1.5

    def attack(self, victim):
        victim.hp -= self.damage
        print(f"{self.name} нанёс тебе {self.damage} урона. Теперь у тебя {victim.hp} здоровья.")
        if victim.hp <= 0:
            exit(print("ПОТРАЧЕНО!"))


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
    "человек": (1, 1),
    "дампир": (1.5, 1.5),
    "зверолюди": (2, 0.8)
}

profs = {
    "лучник": (0.9, 2),
    "щитоносец": (2, 0.6),
    "рыцарь": (1.2, 1.2),
    "колдун": (1.5, 1.5),
    "искатель": (1, 1)
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
print(f"\n\nЗдравствуй, герой с именем {hero.name}!\n" 
      f"Твоё здоровье равно {hero.hp} HP.\n"
      f"Твой урон равен {hero.damage} единицам.\n" 
      f"Желаю удачи в приключениях, странник! 🏹🔪\n")

time.sleep(5)


def fight(victim):
    result = hero.attack(victim)
    time.sleep(2)
    if result:
        victim.attack(hero)
        time.sleep(3)
        fight(victim)
    else:
        print("Ты победил!\n")
        time.sleep(2)
        start()



def start():
    enemy = Enemy()
    print(f"Тебе встретился {enemy.name}. ❤️: {enemy.hp}, ⚔️: {enemy.damage}")
    print("Нападать?")
    answer = input("Да/Нет: ").lower()

    if answer == "да":
        fight(enemy)
    else:
        luck = random.randint(0, 100)

        if luck in range(40):
            print("Ты смог незаметно ускользнуть и пойти дальше!\n")
            time.sleep(2)
            start()
        else:
            print("Проверка удачи провалена! Тебя заметили.\n")
            time.sleep(2)
            enemy.attack(hero)
            fight(enemy)


start()
