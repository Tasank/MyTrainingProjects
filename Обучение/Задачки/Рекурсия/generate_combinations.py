"""
Напишите рекурсивную функцию, которая генерирует все возможные сочетания символов из заданной строки,
не повторяя символы в одной комбинации.
"""

def generate_combinations(s):
    if s == '':
        return ['']
    lst = []
    for i in range(len(s)):
        # Получаем текущий символ
        current = s[i]
        # Генерируем комбинации без текущего символа
        for combination in generate_combinations(s[:i] + s[i + 1:]):
            lst.append(current + combination)

    return lst