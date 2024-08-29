import random
from random import choice

class Paper:
    def __init__(self, size=None):
        self.color_list = ['красный', 'чёрный', 'синий', 'зелёный', 'фиолетовый', 'жёлтый', 'розовый']
        self.material_list = ['офисная', 'глянцевая', 'газетная', 'типографская', 'упаковочная']
        self.size_list = [1500, 3000, 5000, 7000, 10000, 15000, 20000, 25000, 30000, 32000]
        self.color = choice(self.color_list)
        self.material = choice(self.material_list)
        self.size = random.choice(self.size_list)
        self.usable_area = self.size
        self.content = ''


    def __str__(self):
        return f'Это {self.material} бумага размером {self.size} цвета ({self.color}).'

    def take_damage(self, text):
        if self.usable_area <= 0:
            print('Бумага заполнена')
            self.usable_area = 0
        else:
            self.content += text
            self.usable_area -= len(text)
        print(f'В бумаге осталось {self.usable_area} символов.')
        return self


    def info(self):
        # Подсчитываем количество строк и столбцов для вывода содержания бумаги
        rows = int(self.size / 100) + 2  # Добавляем 2 строки для рамки
        cols = int(self.size / 20) + 2  # Добавляем 2 столбца для рамки

        # Выводим верхнюю часть рамки
        print('+' + '-' * (cols - 2) + '+')

        # Выводим содержание бумаги
        lines = self.content.split('\n')
        for i in range(rows - 2):
            line = lines[i] if i < len(lines) else ''
            print('|' + line.ljust(cols - 2) + '|')

        # Выводим нижнюю часть рамки
        print('+' + '-' * (cols - 2) + '+')

        # Выводим информацию о бумаге
        print(f'Это {self.material} бумага размером {self.size} цвета ({self.color}).')
        print(f'В бумаге осталось {self.usable_area} символов.')




class Pen:
    def __init__(self, color=None, material=None, pasta=None):
        """
        Конструктор для класса Pen

        Параметры:
            :param color (str): Цвет пера,
            :param material (str): Материал пера,
            :param pasta (int): Количество пасты в ручке в миллиграммах.

        Returns:
            :return None
        Raises:
            ValueError: Если количество пасты меньше 0.5 или больше 1.2
        """
        self.color_list = ['красный', 'чёрный', 'синий', 'зелёный', 'фиолетовый', 'жёлтый', 'розовый']
        self.material_list = ['шариковая', 'гелевая', 'перьевая', 'капиллярная', 'стираемая']

        if pasta is not None and (pasta < 500 or pasta > 1200):
            self.info()
            raise ValueError('Минимальное количество пасты - 500 миллиграммов, максимальное -1200  миллиграммов')

        self.pasta = pasta
        self.color = self._validate_color(color)
        self.material = self._validate_material(material)

    def _validate_color(self, color):
        if color is None:
            return 'синий'
        elif color.lower() in self.color_list:
            return color
        else:
            return 'синий'

    def _validate_material(self, material):
        if material is None:
            return 'шариковая'
        elif material.lower() in self.material_list:
            return material
        else:
            return 'шариковая'

    def info_pen(self):
        print(f'Это {self.material} ручка, цвета - ({self.color}) .')
        print(f'В ручке {self.pasta} грамм пасты.')

    def mine(self):
        return self.pasta

    def take_damage(self, paper, damage):
        paper = Paper

        self.pasta -= damage

        if self.pasta <= 0:
            print('Ручка утеряна')
            self.pasta = 0

    def info(self):
        print(f'Минимальное количество пасты - 0.5 граммов, максимальное - 1.2 граммов')
        print(f'Возможный цвет ручек - {self.color_list}')
        print(f'Возможный тип ручки - {self.material_list}')


pen_1 = Pen('1', '2', 1000)
pen_1.info_pen()
paper_1 = Paper()
paper_1.info()
