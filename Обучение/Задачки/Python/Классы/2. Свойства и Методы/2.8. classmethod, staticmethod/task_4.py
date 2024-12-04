"""
3. Создайте класс `Person` с classmethod `create_person`, который принимает имя и возраст, и возвращает объект
класса `Person`.
"""
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    @classmethod
    def create_person(cls, name, age):
        return cls(name, age)

    @staticmethod
    def create_person_static(name, age):
        return Person(name, age)

Person.create_person('Вася', 30)
human_1 = Person.create_person('Саня', 25)
print('Метод класса create_person: ', human_1.name)
print(human_1.age)

human_2 = Person.create_person_static('Федя', 8)
print('Метод статической функции create_person_static: ', human_2.name)

print(Person.create_person('Вася', 30).name) # Вася
