class Number:
    def __init__(self, num):
        self.number = num

    def __hash__(self):
        return hash(self.number)

n1 = Number(1)
n2 = Number(1)
n3 = Number('one')

print(n1 == n2)
print(hash(n1))
print(hash(n2))
print(hash(n3))
