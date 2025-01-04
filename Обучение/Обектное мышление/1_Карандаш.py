class Pencil:
    def __init__(self, color: str, size: int, hardness: str, material: str, condition='Новый', reserve=1000):
        self.color = color
        self.size = size
        self.hardness = hardness
        self.material = material
        self.condition = condition
        self.reserve = reserve

    def write(self, text: str):
        if self.reserve > 0:
            self.reserve -= len(text)
            print(text)
            print(f'Грифеля осталось - {self.reserve} символов')
        else:
            print('Грифель закончен.')
            del self

    def info(self):
        print(f'Цвет: {self.color},\n Размер: {self.size},\n Твердость: {self.hardness},\n Материал: {self.material},\n Состояние: {self.condition},\n Количество символов: {self.reserve}')