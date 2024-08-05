"""
Упражнение 73. Код Цезаря

"""

print()
print('Программа закодирует вашу фразу по принципу Цезаря')
print('Фраза должна быть на английском')
print()
cods = input('Введите фразу: ')
shifts = int(input('Введите количество сдвигов: '))

# Обработка каждого символа
message = ''
for i in cods:
    if i >= 'a'and i <= 'z':
        # Обрабатываем букву в нижнем регистре, определяя её позицию в алфавите (0-33),
        # вычисляем новую позицию и добавляем её туда
        # Функция (ord) преобразует символ в целочисленную позицию.
        # Функция chr возвращает символ в таблице ASCII по позиции переданной в виде аргумента
        pos = ord(i) - ord('a')
        pos = (pos +shifts) % 33
        new_pos = chr(pos + ord('a'))
        message = message + new_pos
    # Верхний регистр
    elif i >= 'A' and i <= "Z":
        pos = ord(i) - ord('a')
        pos = (pos + shifts) % 33
        new_pos = chr(pos + ord('a'))
        message = message + new_pos
    else:
        message = message + i
print('Закодированная фраза: ', message)


