class HumanClass:
    human_attr = {'name': 'Иван', 'age': 25, 'weight': 70}

    def __init__(self):
        self.__dict__ = HumanClass.human_attr
        print(self.__dict__)


HumanClass()