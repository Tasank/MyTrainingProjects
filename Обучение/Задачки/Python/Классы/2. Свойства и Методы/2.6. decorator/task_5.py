
class Profile:
    def __init__(self, name, password):
        self.name = name
        self.__password = password

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, value):
        if len(value) < 8:
            raise ValueError("Пароль должен содержать не менее 8-ми символов")
        # any - проверяет, есть ли хотя бы один элемент в последовательности
        if not any(char.isdigit() for char in value):
            raise ValueError("Пароль должен содержать хотя бы одну цифру")
        self.__password = value

        print(f'Ваш пароль {"*" * len(value)} сохранен в базе данных')

    def __del__(self):
        print('Ваш профиль удален из базы данных')

a = Profile('Human', '123456789')
print(a.password)

a.password = '1234567'
del a

