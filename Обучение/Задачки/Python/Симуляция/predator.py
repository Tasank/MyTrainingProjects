"""
Классы животных.
Атрибуты хищников: скорость, обнаружение, выносливость, возраст.
Атрибуты жертв: скорость, скрытность, выносливость, возраст.
Если атрибут скрытность больше атрибута обнаружения, то жертва выживает.
Если атрибуты жертвы больше атрибутов хищников, то жертва выживает и получает потомство + 3
Если наоборот, то хищник убивает жертву, и накапливает + 1 очко, если их накапливается 2, то он получает потомство + 1
Каждый шаг равен 1 году, если оно достигает 12, то оно погибает.
Выигрывает тот кто первый достигает 100 особей
"""
import random


class Predator:
    def __init__(self, speed, detection, endurance, age=0):
        self.speed = speed
        self.detection = detection
        self.endurance = endurance
        self.age = age
        self.points = 0
        self.population = 1

    def hunt(self, prey):
        # Вероятность успешной охоты
        hunting_success_chance = (self.speed / (self.speed + prey.speed)) * (
                    self.detection / (self.detection + prey.stealth))
        if random.random() < hunting_success_chance:
            if prey.speed > self.speed and prey.endurance > self.endurance:
                prey.population += 3  # Жертва выживает и получает потомство
                return False
            else:
                self.points += 1
                self.population += 1  # Увеличиваем популяцию хищников за каждое убийство
                if self.points >= 2:
                    # Увеличиваем популяцию
                    if random.random() < 0.5:  # 50% шанс на воспроизводство
                        self.population += 1  # Хищник получает потомство
                    self.points = 0
                return True  # Хищник убивает жертву
        else:
            return False  # Жертва выживает

    def age_one_year(self):
        self.age += 1
        if self.age >= 12:
            self.population -= 1


class Prey:
    def __init__(self, speed, stealth, endurance, age=0):
        self.speed = speed
        self.stealth = stealth
        self.endurance = endurance
        self.age = age
        self.population = 1

    def age_one_year(self):
        self.age += 1
        if self.age >= 12:
            self.population -= 1

    def reproduce(self):
        # Увеличиваем популяцию жертв раз в несколько лет
        if random.random() < 0.5:  # 50% шанс на воспроизводство
            self.population += 2


def simulate(predator, prey):
    year = 0
    while predator.population < 100 and prey.population < 100:
        year += 1
        print(f"Год {year}:")

        # Взаимодействие хищника и жертвы
        if predator.hunt(prey):
            prey.population -= 1  # Если хищник убил жертву
            print("Хищник убил жертву.")
        else:
            print("Жертва выжила.")

        # Старение хищников и жертв
        predator.age_one_year()
        prey.age_one_year()

        # Популяция жертв может увеличиваться
        prey.reproduce()

        print(f"Популяция хищников: {predator.population}")
        print(f"Популяция жертв: {prey.population}")

        if predator.population <= 0 or prey.population <= 0:
            break

    if predator.population >= 100:
        print("Хищники победили!")
    elif prey.population >= 100:
        print("Жертвы победили!")
    else:
        print("Симуляция завершилась преждевременно из-за вымирания.")


# Инициализация объектов
predator = Predator(speed=random.randint(1, 10), detection=random.randint(1, 10), endurance=random.randint(1, 10))
prey = Prey(speed=random.randint(1, 10), stealth=random.randint(1, 10), endurance=random.randint(1, 10))

# Запуск симуляции
simulate(predator, prey)


