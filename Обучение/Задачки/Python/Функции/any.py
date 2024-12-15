"""
Функция any() возвращает True, если хотя бы один элемент истинен, в противном случае — False.
"""
focus_list = [1, 2, 3, 4, 5, '12', False]
num_list = []
str_list = []

for f in focus_list:
    if int == type(f):
        num_list.append(f)
    elif str == type(f):
        str_list.append(f)
    else:
        print('Найден незарегистрированный тип данных')

print('Список чисел: ', *num_list)
print(f'Список строк: {str_list}')
