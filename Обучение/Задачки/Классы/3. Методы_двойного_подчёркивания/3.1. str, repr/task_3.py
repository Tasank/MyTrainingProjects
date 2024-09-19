
class Enemy:
    def __init__(self, *args):
        self.warriors = [x for x in args if isinstance(x, str)]

    def __str__(self):
        return f'Наблюдаемые войска: {tuple(self.warriors)}'

    def __repr__(self):
        return f'Название класса: {self.__class__.__name__}, \nАтрибуты класса: {self.__dict__} '


w1 = Enemy('Стрелок', 'Снайпер', 'Артиллерист', 'Солдат', 'Пехотинец',
           'Пехотинец', 'Пехотинец', 'Артиллерист', 'Солдат', 'Стрелок')
print(w1)
print(repr(w1))
