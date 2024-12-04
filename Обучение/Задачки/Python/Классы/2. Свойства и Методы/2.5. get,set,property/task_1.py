class House:
    def __init__(self, owner, castle):
        self.owner = owner
        self.rooms = []
        self.__castle = castle

    def add_room(self, room):
        self.rooms.append(room)
        print(f'Комнаты в доме: {self.rooms}')
    # Это приватное свойство get получает значение castle
    def get_castle(self):
        print('Получить замок')
        return self.__castle
    # Это приватное свойство set устанавливает значение castle
    def set_castle(self, value):
        print('Установить замок')
        self.__castle = value
    # Это приватное свойство del удаляет значение castle
    def del_castle(self):
        print('Удалить замок')
        del self.__castle
    # Определить свойство castle (get, set, del) - (прочитать, установить, удалить)
    castle = property(fget=get_castle, fset=set_castle, fdel=del_castle)

my_house = House('Владелец', 0000)

my_house.add_room('Комната 1')
my_house.castle # get
my_house.castle = 1000 # set
del my_house.castle # del

