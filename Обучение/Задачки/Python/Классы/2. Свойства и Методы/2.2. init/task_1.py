class Color:
    def __init__(self, name):
        self.name = name
    def is_true(self):
        color_list = ['белый', 'чёрный', 'зелёный', 'красный', 'синий', 'фиолетовый', 'жёлтый', 'розовый']
        if self.name in color_list:
            print(f'Цвет ({self.name}) есть в списке. Его индекс - {color_list.index(self.name)}')
        else:
            print('Цвета нет в списке')


red = Color('красный')
red.is_true()