"""
Упражнение 77. Таблица умножения.
Вывести в консоль таблицу умножения от 1 до 10.
"""
print('   1 2 3 4 5 6 7 8 9 10')
a = 1
table = range(1, 11)
for i in table:
    print(i, end = "| ")
    mult = [num * i for num in table]
    print(*mult,)


