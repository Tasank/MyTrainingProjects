import random
import string


class Probe:
    def __init__(self, id, energy, resources, errors=0, intelligence=0, aggression_level=0):
        self.id = id
        self.energy = energy
        self.resources = resources
        self.errors = errors
        self.intelligence = intelligence
        self.aggression_level = aggression_level  # Уровень агрессии зонда

    def clone(self):
        new_id = self.generate_new_id()
        new_errors = self.errors + random.randint(0, 3)  # Возможность накопления ошибок
        new_intelligence = self.intelligence + random.choice([0, 1])
        new_aggression = self.aggression_level + random.randint(0, 2)  # Увеличение агрессии
        return Probe(new_id, self.energy, self.resources.copy(), new_errors, new_intelligence, new_aggression)

    @staticmethod
    def generate_new_id(length=6):
        characters = string.ascii_uppercase + string.digits
        return ''.join(random.choice(characters) for _ in range(length))

    def make_decision(self):
        """Зонд принимает решение на основе своего интеллекта и агрессии."""
        if self.intelligence > 5:
            self.aggression_level += 1  # Увеличение уровня агрессии
            print(f"{self.id} становится агрессивным. Уровень агрессии: {self.aggression_level}")
            if self.aggression_level > 5:
                print(f"{self.id} начинает нападение на другие зонды!")
        elif self.errors > 10:
            print(f"{self.id} испытывает критические ошибки и теряет контроль!")
            self.energy = 0  # Зонд теряет всю энергию

    def resource_depletion(self):
        """Уменьшает ресурсы через время."""
        for resource in list(self.resources.keys()):
            depletion = random.randint(0, 10)
            if self.resources[resource] > depletion:
                self.resources[resource] -= depletion
            else:
                del self.resources[resource]  # Ресурс истощен
                print(f"{self.id} истощил ресурс: {resource}")

    def __str__(self):
        return (f"Зонд ID: {self.id}, Энергия: {self.energy}, Ошибки: {self.errors}, "
                f"Интеллект: {self.intelligence}, Агрессия: {self.aggression_level}")


def simulate_probes(num_probes):
    initial_probe = Probe("000001", energy=100, resources={"никель": 500, "медь": 300, "вода": 1000, "кислород": 500})
    probes = [initial_probe]

    for _ in range(1, num_probes):
        new_probe = probes[-1].clone()
        probes.append(new_probe)

    return probes


def analyze_probes(probes):
    first_probe = probes[0]
    last_probe = probes[-1]

    print(f"\nПервый зонд: {first_probe}")
    print(f"Последний зонд: {last_probe}")

    # Оценка изменений
    if last_probe.errors > first_probe.errors:
        print("Последний зонд накопил больше ошибок.")
    if last_probe.intelligence > first_probe.intelligence:
        print("Последний зонд стал более интеллектуальным.")
    if last_probe.aggression_level > 5:
        print("Последний зонд стал разумным и начинает агрессивные действия!")

    # Проверка на истощение ресурсов
    depleted_resources = [res for res in last_probe.resources if last_probe.resources[res] <= 0]
    if depleted_resources:
        print(f"Последний зонд истощил ресурсы: {', '.join(depleted_resources)}")


def run_simulation(num_probes):
    probes = simulate_probes(num_probes)
    for probe in probes:
        probe.make_decision()
        probe.resource_depletion()
    analyze_probes(probes)


# Симуляция 10000 зондов
num_probes = 10000
run_simulation(num_probes)
