class PlayerUser:
    def __init__(self, nick, age, password):
        self.nick = nick
        self.age = age
        self.password = password
    def full_name(self):
        return f'{self.nick} {self.age}'
    def is_adult(self):
        return self.age >= 18

    def check_password(self, password):
        return self.password == password

    def pvp(self):
        password = input('Введите пароль: ')
        if self.check_password(password):
            if self.is_adult():
                print(f'Игрок {self.nick} может сражаться в PVP')
            else:
                print(f'Игрок [{self.nick}] не может сражаться в PVP')
        else:
            print('Неверный пароль')

noob = PlayerUser('noob', 12, '123456')

noob.pvp()