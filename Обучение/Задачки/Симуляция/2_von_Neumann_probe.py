import random
import string


class Probe:
    def __init__(self, id, energy, resources, errors=0, intelligence=0):
        self.id = id
        self.energy = energy
        self.resources = resources
        self.errors = errors  # Количество ошибок
        self.intelligence = intelligence  # Уровень интеллекта

    def clone(self):
        # Клонирование зонда с возможностью изменения его состояния
        new_id = self.generate_new_id()
        new_errors = self.errors + random.randint(0, 2)  # Возможность накопления ошибок
        new_intelligence = self.intelligence + random.choice([0, 1])  # Увеличение интеллекта
        return Probe(new_id, self.energy, self.resources.copy(), new_errors, new_intelligence)

    @staticmethod
    def generate_new_id(length=6):
        characters = string.ascii_uppercase + string.digits
        return ''.join(random.choice(characters) for _ in range(length))

    def __str__(self):
        return f"Зонд ID: {self.id}, Энергия: {self.energy}, Ошибки: {self.errors}, Интеллект: {self.intelligence}"


def simulate_probes(num_probes):
    initial_probe = Probe("000001", energy=100, resources={"никель": 500, "медь": 300})
    probes = [initial_probe]

    for _ in range(1, num_probes):
        new_probe = probes[-1].clone()
        probes.append(new_probe)

    return probes


def analyze_probes(probes):
    first_probe = probes[0]
    last_probe = probes[-1]

    print(f"Первый зонд: {first_probe}")
    print(f"Последний зонд: {last_probe}")

    # Оценка изменений
    if last_probe.errors > first_probe.errors:
        print("Последний зонд накопил больше ошибок.")
    if last_probe.intelligence > first_probe.intelligence:
        print("Последний зонд стал более интеллектуальным.")

    # Пример возможной логики для войны
    if last_probe.intelligence > 5:  # Условие для начала войны
        print("Последний зонд стал разумным и может начать войну!")


# Симуляция 10000 зондов
num_probes = 10000
probes = simulate_probes(num_probes)
analyze_probes(probes)
