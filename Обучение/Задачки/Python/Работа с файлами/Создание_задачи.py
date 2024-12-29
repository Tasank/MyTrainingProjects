"""
Этот код создает простой .py файл,
который содержит свой рабочий python код.
"""

filename = 'Простой_алгоритм.py'
with open(filename, 'w') as file:
    content = ('num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]\n'
               'new_list = []\n'
               'for num in num_list:\n'
               '    new_list.append(num)\n'
               'print(*new_list)')
    file.write(content)