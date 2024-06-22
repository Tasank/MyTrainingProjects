"""
Упражнение 153. Самое длинное слово в файле.
В данном упражнении вы должны написать программу, которая будет находить самое длинное слово в файле. В
качестве результата программа должна выводить на экран длину самого длинного слова и все слова такой длины.
Для простоты принимайте за значимые буквы любые непробельные символы, включая цифры и знаки препинания.
"""
def check_longest_words(filename):
    """
    Находит самое длинное слово в файле и возвращает его длину, а также все слова такой длины.

    :param filename: Имя файла, в котором необходимо найти самое длинное слово.
    :type filename: str
    :return: Кортеж, содержащий длину самого длинного слова и список всех слов такой длины.
    :rtype: tuple (int, list of str)
    """
    # Инициализируем список для хранения самых длинных слов
    longest_words = []
    # Инициализируем переменную для хранения длины самого длинного слова
    max_length = 0

    with open(filename, 'r') as readfile:
        for line in readfile:
            # Разбить строку на слова
            words = line.split()
            for word in words:
                word_length = len(word)
                # Если длина текущего слова больше max_length, обновляем max_length и сбрасываем список longest_words,
                # добавив туда текущее слово.
                if word_length > max_length:
                    max_length = word_length
                    longest_words = [word]
                elif word_length == max_length:
                    longest_words.append(word)
    return max_length, longest_words


# Имя файла
filename = 'test.txt'

# Получаем длину самого длинного слова и все слова такой длины
max_length, longest_words = check_longest_words(filename)

# Выводим результат
print(f'Длина самого длинного слова: {max_length}')
print('Слова такой длины:', ', '.join(longest_words))
