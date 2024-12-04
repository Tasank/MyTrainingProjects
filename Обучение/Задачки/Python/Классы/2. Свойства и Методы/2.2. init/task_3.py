from task_2 import Warrior

class Battle:
    """
    Класс, представляющий бой между двумя воинами.
    """

    def __init__(self, warrior_1_name, warrior_2_name):
        """
        Инициализация боя.

        :param warrior_1_name: имя первого воина
        :param warrior_2_name: имя второго воина
        """
        self.warrior_1 = Warrior(warrior_1_name)
        self.warrior_2 = Warrior(warrior_2_name)
        self.count_1 = 0
        self.count_2 = 0

    def _check_initiative(self, warrior_1, warrior_2):
        """
        Проверка инициативы.

        :param warrior_1: первый воин
        :param warrior_2: второй воин
        :return: True, если первый воин имеет инициативу, False - если второй
        """
        if warrior_1.agility > warrior_2.agility:
            return True
        elif warrior_1.agility < warrior_2.agility:
            return False
        else:
            return None

    def _check_strength(self, warrior_1, warrior_2):
        """
        Проверка силы.

        :param warrior_1: первый воин
        :param warrior_2: второй воин
        :return: True, если первый воин имеет большую силу, False - если второй
        """
        if warrior_1.strength > warrior_2.strength:
            return True
        elif warrior_1.strength < warrior_2.strength:
            return False
        else:
            return None

    def fight(self):
        """
        Начало боя.
        """
        while self.warrior_1.stamina > 0 and self.warrior_2.stamina > 0:

            initiative = self._check_initiative(self.warrior_1, self.warrior_2)

            if initiative is True:
                self.warrior_2.stamina -= 1
                self.count_1 += 1
                print(f'Боец ({self.warrior_1.name}) наносит быстрый удар по бойцу ({self.warrior_2.name})')
            elif initiative is False:
                self.warrior_1.stamina -= 1
                self.count_2 += 1
                print(f'Боец ({self.warrior_2.name}) наносит быстрый удар по бойцу ({self.warrior_1.name})')
            else:
                print('Бойцы не могут взять инициативу')
                self.warrior_1.stamina -= 1
                self.warrior_2.stamina -= 1

            strength = self._check_strength(self.warrior_1, self.warrior_2)

            if strength is True:
                self.warrior_2.stamina -= 1
                self.count_1 += 2
                print(f'Боец ({self.warrior_1.name}) наносит мощный удар по бойцу ({self.warrior_2.name})')
            elif strength is False:
                self.warrior_1.stamina -= 1
                self.count_2 += 2
                print(f'Боец ({self.warrior_2.name}) наносит мощный удар по бойцу ({self.warrior_1.name})')

        if self.count_1 > self.count_2:
            print(f'\n Победил {self.warrior_1.name}')
        else:
            print(f'\n Победил {self.warrior_2.name}')

        print(f'Количество очков {self.warrior_1.name}: {self.count_1}')
        print(f'Количество очков {self.warrior_2.name}: {self.count_2}')


round_1 = Battle('Максим', 'Александр')
round_1.fight()
