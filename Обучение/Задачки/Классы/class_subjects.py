import random
from random import choice

class Paper:
    def __init__(self, size=None):
        self.color_list = ['красный', 'чёрный', 'синий', 'зелёный', 'фиолетовый', 'жёлтый', 'розовый']
        self.material_list = ['офисная', 'глянцевая', 'газетная', 'типографская', 'упаковочная']
        self.color = choice(self.color_list)
        self.material = choice(self.material_list)
        self.size = random.uniform(0.5, 1.2) if size is None else size

    def info_paper(self):
        print(f'Это {self.material} бумага размером {self.size} цвета ({self.color}).')


class Pen:
    def __init__(self, color=None, material=None, pasta=None):
        """
        Конструктор для класса Pen

        Параметры:
            :param color (str): Цвет пера,
            :param material (str): Материал пера,
            :param pasta (int): Количество пасты в ручке в граммах.

        Returns:
            :return None
        Raises:
            ValueError: Если количество пасты меньше 0.5 или больше 1.2
        """
        self.color_list = ['красный', 'чёрный', 'синий', 'зелёный', 'фиолетовый', 'жёлтый', 'розовый']
        self.material_list = ['шариковая', 'гелевая', 'перьевая', 'капиллярная', 'стираемая']

        if pasta is not None and (pasta < 0.5 or pasta > 1.2):
            self.info()
            raise ValueError('Минимальное количество пасты - 0.5 граммов, максимальное - 1.2 граммов')

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
    info_pen()

    def info(self):
        print(f'Минимальное количество пасты - 0.5 граммов, максимальное - 1.2 граммов')
        print(f'Возможный цвет ручек - {self.color_list}')
        print(f'Возможный тип ручки - {self.material_list}')


pen_1 = Pen('1', '2', 1)
pen_1.info_pen()