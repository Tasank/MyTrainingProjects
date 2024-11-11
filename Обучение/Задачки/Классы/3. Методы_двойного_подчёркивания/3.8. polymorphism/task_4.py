"""
Создайте класс FigureFactory, который может создавать объекты любого из классов Rectange,
Square или Circle в зависимости от переданных параметров.
"""
from task_3 import Rectangle, Square, Circle


class FigureFactory:
    def __init__(self):
        self.figure = None

    def create_figure(self, figure_type, *args):

        if figure_type.lower() == 'rectangle':
            print('Создан прямоугольник')
            self.figure = Rectangle(*args)

        elif figure_type.lower() == 'square':
            print('Создан квадрат')
            self.figure = Square(*args)

        elif figure_type.lower() == 'circle':
            print('Создан круг')
            self.figure = Circle(*args)

        else:
            print('Такой фигуры не предусмотренно')

        return self.figure


f = FigureFactory()

r = f.create_figure('rectangle', 5, 10)
print(r.get_perimeter())  # 30
