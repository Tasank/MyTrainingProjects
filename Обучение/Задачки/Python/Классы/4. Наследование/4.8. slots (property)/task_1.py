class Human:
    __slots__ = 'name', 'age', '__phone'

    def __init__(self, name, age, phone):
        self.name = name
        self.age = age
        self.phone = phone

    @property
    def phone(self):
        print('Телефон:')
        return self.__phone

    @phone.setter
    def phone(self, value):
        print(f'Новый номер телефона: {value}')
        self.__phone = value

class Man(Human):
    __slots__ = 'gender'

    def __init__(self, name, age, phone):
        super().__init__(name, age, phone)
        self.gender = 'мужской'

Dima = Man('Дмитрий', 20, '1234-56-78') # Новый номер телефона: 1234-56-78

Dima.phone # Телефон:
