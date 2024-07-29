"""
Упражнение 53. Числовые оценки – в буквенные.
В предыдущем упражнении мы переводили буквенные оценки студентов в числовые.
Сейчас перевернем ситуацию и попробуем определить буквенный номинал оценки по его числовому эквиваленту.
Убедитесь в том, что ваша программа будет обрабатывать числовые значения между указанными в табл. 2.13.
В этом случае оценки должны быть округлены до ближайшей буквы. Программа должна выдавать оценку A+,
если введенное пользователем значение будет 4,0 и выше.
"""

estimation = float(input('Введите числовую оценку: '))

if estimation >= 4:
    result = 'A+'
elif 4 > estimation > 3.7:
    result = 'A'
elif 3.7 >= estimation > 3.3:
    result = 'A-'
elif 3.3 >= estimation > 3:
    result = 'B+'
elif 3 >= estimation > 2.7:
    result = 'B'
elif 2.7 >= estimation > 2.3:
    result = 'B-'
elif 2.3 >= estimation > 2:
    result = 'C+'
elif 2 >= estimation > 1.7:
    result = 'C'
elif 1.7 >= estimation > 1.3:
    result = 'C-'
elif 1.3 >= estimation > 1:
    result = 'D+'
elif 1 >= estimation > 0:
    result = 'D'
elif estimation == 0:
    result = 'F'
else:
    print('Неправильный ввод: ')
    quit()

print(f'Числовая оценка - ({estimation}) равняется буквенной - ({result})')
