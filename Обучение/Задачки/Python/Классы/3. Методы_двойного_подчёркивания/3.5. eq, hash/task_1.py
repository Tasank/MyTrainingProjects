class Human:
    def __init__(self, name, age, gender='Мужской'):
        self.name = name
        self. age = age
        self.gender = gender

    def __eq__(self, other):
        return self.name == other.name and self.age == other.age and self.gender == other.gender

    def __hash__(self):
        return hash((self.name, self.age, self.gender))

Mihail = Human('Михайл', 25)
Ivan = Human('Иван', 25)

print(Mihail == Ivan)

print(hash(Mihail))
print(hash(Ivan))