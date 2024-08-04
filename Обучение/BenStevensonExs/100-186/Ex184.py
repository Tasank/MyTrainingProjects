"""
Упражнение 184. Выравниваем список.
Напишите функцию, реализующую рекурсивный алгоритм выравнивания списка, описанный выше. Функция должна принимать на
вход список и возвращать выровненную версию списка. В основной программе продемонстрируйте работу функции на примере
приведенного выше списка, а также нескольких других.
"""
def flatten(data):
    if not data:  # Если список пустой
        return []

    first_element = data[0]
    rest_of_elements = data[1:]

    if isinstance(first_element, list):  # Если первый элемент тоже список
        return flatten(first_element) + flatten(rest_of_elements)
    else:  # Если первый элемент не список
        return [first_element] + flatten(rest_of_elements)

def main():
    # Пример использования, словарь списков которые нужно выровнять
    nested_dict = {
        '1': [1, [2, 3], [4, [5, [6, 7]]], [[[8], 9], [10]]],
        '2': [[1, 2, [3, 4]], [5, [6, 7]], 8, [9, [10]]],
        '3': [[], [1, [2, [3, [4, [5]]]]]]
        }
    # Вызываем функцию выравнивания для каждого значения ключа (1,2 и 3) в словаре
    for nested_list in nested_dict:
        flattened_list = flatten(nested_dict[nested_list])
        print(flattened_list)

if __name__ == '__main__':
    main()
