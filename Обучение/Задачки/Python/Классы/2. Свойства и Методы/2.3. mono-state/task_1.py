
class Robot:
    robot_info_attr = {
        'i1': '0000А1',
        'i2': 'Уборщик',
        'i3': '2 месяца',
    }
    def __init__(self):
        self.__dict__ = Robot.robot_info_attr
        print(self.__dict__)

N1 = Robot()
N2 = Robot()
N3 = Robot()
N3.i1 = '0000А2'
N3.i2 = 'Садовник'
N3.i3 = '6 месяцев'
N3 = Robot()
