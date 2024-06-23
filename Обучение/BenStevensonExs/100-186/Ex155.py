"""
Упражнение 155. Частота слов в файле.
Разработайте программу, которая будет показывать слово (или слова), чаще остальных встречающееся
в текстовом файле. Сначала пользователь должен ввести имя файла для обработки.
После этого вы должны открыть файл и проанализировать его построчно, разделив при этом строки по
словам и исключив из них пробелы и знаки препинания. Также при подсчете частоты появления слов в
файле вам стоит игнорировать регистры.
"""

def most_frequent_words(filename):
    word_counts = Counter()

    with open(filename, 'r') as file:
        for line in file:
            # Приведение строки к нижнему регистру и удаление знаков препинания
            cleaned_line = clean_text(line.lower())
            words = cleaned_line.split()
            word_counts.update(words)

    # Нахождение максимальной частоты
    max_frequency = max(word_counts.values(), default=0)

    # Нахождение слов с максимальной частотой
    most_frequent = [word for word, count in word_counts.items() if count == max_frequency]

    return most_frequent, max_frequency


filename = input('Введите имя файла для обработки: ')
words, frequency = most_frequent_words(filename)
print(f'Самое частое слово(а): {", ".join(words)} (встречается {frequency} раз)')

