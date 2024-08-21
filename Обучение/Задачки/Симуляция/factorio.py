"""
Симуляция должна запускаться после ввода кол-во часов симуляции. По итогу должен вывести смерть /победа / или текущий
прогресс персонажа за прошедшее время. Результат должен вывести подробную информацию, о постройках персонажа,
его улучшениях, его броне, добытых ресурсах.

1) Генерация руды.
## Зависит от уровня развития местности (карты), карта не бесконечна. У руды есть заканчиваемый ресурс
- Уголь, Железо, медь, камень, (уран, нефть)

2) Добыча ресурсов
## Тратится время

3) Производство
# Материалы будут изготавливаться персонажем моментально

4) Уровень загрязнения
## Увеличивается от некоторых машин

5) Военная промышленность
## Увеличивает шанс выживаемости персонажа. Нужно для обороны объектов. Необходимы улучшения технологий *лаборатория

6) Энергия
## Необходимы для машин

7) Лаборатория
## Тратится время для открытия улучшения

8) Условия победы
## Уничтожение всех монстров на планете/ Постройка ракеты

9) Условия проигрыша
# Смерть персонажа

"""

# Функция жизни человека
# @param armor_modifier - Модификатор брони, увеличивает броню на это кол-во
# @param weapon_modifier - Модификатор урона от оружия
# @param damage_modifier - Модификатор полученного урона от монстров
# @param mining_speed_modifier - Модификатор увеличения скорости добычи ресурсов (Зависит от улучшений)
# @return здоровье, урон, скорость добычи
def human(armor_modifier=0, weapon_modifier=0, damage_modifier=0, mining_speed_modifier=0):
    health = 100
    armor = 0 + armor_modifier
    damage = 5 + weapon_modifier
    mining_speed = 0.5 + mining_speed_modifier

    if damage_modifier > armor:
        armor = 0
        damage_modifier -= armor
        health = 100 - damage_modifier
    else:
        armor -= damage_modifier

    return health, damage, mining_speed


health, damage, mining_speed = human()
print(mining_speed)

# Класс твердотельного бура возвращает кол-во прочности, скорость добычи и загрязнения
# @param deposit - ресурс в месторождении
# @param coal - угль необходимый для работы бура
# @param endurance_damage - Модификатор изменения прочности
# @return добытый ресурс, прочность, загрязнение
class Solid_State_Drill:
    def __init__(self, deposit, coal, endurance_damage=0, mining_speed_modifier=0):
        self.deposit = deposit
        self.coal = coal
        self.endurance_damage = endurance_damage
        self.mining_speed_modifier = mining_speed_modifier

    endurance = 700 + endurance_damage
    mining_speed = 0.25 + mining_speed_modifier

    if coal < 1:
        extracted_deposit = 0
        pollution = 0
        return endurance
    else:
        extracted_deposit = 1
        pollution = 12
        return endurance,