"""
Вы работаете над модулем внутрикорпоративной системы учета данных сотрудников компании. Программа должна:
1)Найти сотрудника с минимальным возрастом;
2)Вычислить медианный возраст всех сотрудников.
3) Найти сотрудника с максимальным возрастом.
Медиана — число, которое находится в середине этого набора, если его упорядочить по возрастанию.
Если набор чисел четный, то берется среднее между двумя средними числами и округляется до целого.
Формат ввода
Первая строка содержит данные сотрудников. Данные включают имя, возраст и отдел, разделенные запятой, без пробелов.
Информация о каждом сотруднике отделена от других через точку с запятой. Количество сотрудников — от 2 до 100.

Формат вывода
Вторая строка содержит три целых числа, разделенные пробелом: минимальный возраст,
медианный возраст и максимальный возраст.

Пример 1
Входные данные:
Иван,28,Инженер;Олег,34,HR;Денис,45,Маркетинг;Анна,30,Инженер;Борис,24,HR

Выходные данные:
24 30 45

Пример 2
Входные данные:
Павел,28,Инженер;Елена,34,Маркетинг

Выходные данные:
28 31 34
"""


def process_employee_data(input_string: str) -> str:
    # Разделяем информацию о каждом сотруднике
    employees = input_string.split(';')

    # Извлекаем возраст каждого сотрудника
    ages = [int(employee.split(',')[1]) for employee in employees]

    # Находим минимальный и максимальный возраст
    min_age = min(ages)
    max_age = max(ages)

    # Вычисляем медианный возраст
    ages.sort()
    n = len(ages)
    if n % 2 == 1:
        median_age = ages[n // 2]
    else:
        median_age = round((ages[n // 2 - 1] + ages[n // 2]) / 2)

    # Формируем строку вывода
    return f"{min_age} {median_age} {max_age}"


# Пример использования
input_data = input()
output_data = process_employee_data(input_data)
print(output_data)

