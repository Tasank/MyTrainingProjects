class Cat:
    name = 'Егерь'
    color = 'Пёстрый'
    age = 5

objects_list = []

for _ in range(150):
    objects_list.append(Cat())

print(objects_list)
print(len(objects_list))