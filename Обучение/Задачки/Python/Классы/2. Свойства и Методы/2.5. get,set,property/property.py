class Person:
    def __init__(self, name, age):
        self._name = name
        self.age = age

    @property # get
    def name(self):
        return self._name

    @name.setter # set
    def name(self, value):
        if not isinstance(value, str):
            raise ValueError("Имя должно быть строкой")
        self._name = value

    @name.deleter # del
    def name(self):
        del self._name

person = Person("Саня", 25)
print(person.name)  # выводит "Саня"

person.name = "Раф"
print(person.name)  # выводит "Раф"

del person.name

try:
    print(person.name)
except AttributeError:
    print("Атрибут name удален")
