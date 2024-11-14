"""
 Создайте новый класс Nurse, который является подклассом Person. Переопределите метод walk,
 чтобы он печатал "Nurse может ходить быстро". Создайте экземпляр Nurse и вызовите метод _info.
"""
class Person:
    def __init__(self, name):
        self.name = name
        self.race = 'Голая обезьяна'

    def walk(self):
        print(f'{self.name} может ходить')

    def _info(self):
        print()
        print(f'Класс: {self.__class__.__name__}')
        print(f'Имя: {self.name} \nРаса: {self.race}')

class Nurse(Person):
    def __init__(self, experience, name):
        super().__init__(name)
        if isinstance(experience, int) and 0 <= experience < 80:
            self.experience = experience
        else:
            raise ValueError('Неверное значение опыта')

    def walk(self):
        print('Медсестра может ходить быстро')

    def _info(self):
        super()._info()
        print(f'Опыт работы: {self.experience}', end="\n\n")


nurse = Nurse(10, 'Алина')
print(nurse.race) # Голая обезьяна
nurse.walk()
nurse._info()

human = Person('Вася')
human._info()
# print(human.experience) # AttributeError: 'Person' object has no attribute 'experience'
