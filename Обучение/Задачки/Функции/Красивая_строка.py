"""
Задача. Вывести кол-во изменений необходимое для изменения двоичной строки (0/1),
в число-палиндром (011) -> (101) Вывод: 1
"""
def string(s):
    count = 0
    prev_char = ''
    prev_count = 0
    for char in s:
        if char == prev_char:
            prev_count += 1
        else:
            count += prev_count // 2
            prev_char = char
            prev_count = 1
    count += prev_count // 2
    return count
s = input('Введите двоичное число(из 0 и 1): ')
result = string(s)
print('Кол-во необходимых изменений для превращения в палиндром: ', result)