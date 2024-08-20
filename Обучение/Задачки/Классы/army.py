"""
Классы состав Армий.
"""

class Army:
    def __init__(self):
        self.ground_forces = {
            "Motor Rifle Troops": 0,
            "Tank Troops": 0,
            "Artillery and Rocket Troops": 0,
            "Air Defense Troops": 0,
            "Engineering Troops": 0
        }
        self.aerospace_forces = {
            "Air Force": 0,
            "Space Forces": 0,
            "Air and Missile Defense Forces": 0
        }
        self.navy = {
            "Surface Forces": 0,
            "Submarine Forces": 0,
            "Naval Aviation": 0,
            "Coastal Troops": 0,
            "Naval Infantry": 0
        }
        self.airborne_forces = {
            "Parachute Units": 0,
            "Assault Units": 0
        }
        self.strategic_rocket_forces = {
            "Mobile Missile Systems": 0,
            "Silo Launchers": 0
        }
        self.special_forces = {
            "Reconnaissance Units": 0,
            "Electronic Warfare Troops": 0,
            "Chemical Protection Troops": 0
        }
        self.logistics = {
            "Rear Units": 0,
            "Medical Service": 0,
            "Transport Troops": 0
        }

    def update_unit_count(self, category, unit_name, count):
        if category in self.__dict__:
            if unit_name in self.__dict__[category]:
                self.__dict__[category][unit_name] = count
            else:
                print(f"Данный юнит '{unit_name}' не найден в категории '{category}'")
        else:
            print(f'Данная категория "{category}" не найдено')

    def get_unit(self, category, unit_name):
        if category in self.__dict__:
            return self.__dict__[category].get(unit_name,
                                               'Подразделение не найдено!')
        return 'Категория не найдена.'

RussianArmy = Army()

# Обновляем количество войск
RussianArmy.update_unit_count('ground_forces', 'Motor Rifle Troops', 280000)
RussianArmy.update_unit_count('ground_forces', 'Tank Troops', 13000)
RussianArmy.update_unit_count('ground_forces', 'Artillery and Rocket Troops', 20000)
RussianArmy.update_unit_count('ground_forces', 'Air Defense Troops', 10000)
RussianArmy.update_unit_count('ground_forces', 'Engineering Troops', 15000)

RussianArmy.update_unit_count('aerospace_forces', 'Air Force', 190000)
RussianArmy.update_unit_count('aerospace_forces', 'Space Forces', 50000)
RussianArmy.update_unit_count('aerospace_forces', 'Air and Missile Defense Forces', 40000)

RussianArmy.update_unit_count('navy', 'Surface Forces', 150000)
RussianArmy.update_unit_count('navy', 'Submarine Forces', 60000)
print(RussianArmy.get_unit("ground_forces", "Motor Rifle Troops"))