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

    # Добавление босса Кентавра
    def init(self, is_boss=False):
        if is_boss:
            self.name = "Кентавр"
            self.hp = 500
            self.damage = 250
            self.xp = 0  # Босс не дает опыта
        else:
            self.name = random.choice(list(self.races.keys()))
            self.hp = self.races[self.name][0]
            self.damage = self.races[self.name][1]
            self.xp = self.hp * 1.5