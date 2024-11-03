class Human:
    def __init__(self, name, age, gender='Мужской'):
        self.name = name
        self. age = age
        self.gender = gender

    def __eq__(self, other):
        return self.name == other.name and self.age == other.age and self.gender == other.gender

    def __hash__(self):
        return hash((self.name, self.age, self.gender))

    def __bool__(self):
        return self.age >= 18

Bob = Human('Bob', 19)
Sanya = Human('Санчоус', 17)

print(bool(Bob))
print(bool(Sanya))