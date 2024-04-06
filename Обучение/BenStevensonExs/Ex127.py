"""
Упражнение 127. Список уже отсортирован?
Напишите функцию, показывающую, отсортирован ли переданный ей в качестве параметра список
(по возрастанию или убыванию). Функция должна возвращать True, если список отсортирован,
и False в противном случае. В основной программе запросите у пользователя последовательность чисел для списка,
после чего выведите сообщение о том, является ли этот список отсортированным изначально.
"""
def sort_list_check(numbers_list):
    sorting_list = sorted(numbers_list)
    if numbers_list == sorting_list:
        return True
    else:
        return False

def ask():
    numbers_list = []
    numbers = input('Введите число: ')
    while True:
        if not numbers:
            break
        numbers_list.append(int(numbers))
        numbers = input('Введите число (Enter для выхода): ')

    if sort_list_check(numbers_list):
        print(f'Это отсортированный список: {numbers_list}')
    else:
        print('Этот список не отсортирован.')

ask()