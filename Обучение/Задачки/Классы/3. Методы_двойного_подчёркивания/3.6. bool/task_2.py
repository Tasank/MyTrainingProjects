class House:
    def __init__(self, *args):
        self.rooms = []

        for i in args:
            self.rooms.append(i)

    def __len__(self):
        return len(self.rooms) <= 4


h1 = House('a', 'b', 'c')
print(h1.rooms)
print(bool(h1)) # True

h2 = House('a', 'b', 'c', '4', '5')
print(bool(h2)) # False