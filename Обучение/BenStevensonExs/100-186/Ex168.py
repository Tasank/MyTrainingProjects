"""
Упражнение 168. Повторяющиеся слова.
В данном упражнении вам предстоит написать программу для определения наличия дублей слов в тексте.
При нахождении повтора на экран должен выводиться номер строки и дублирующееся слово. Удостоверьтесь,
что программа корректно обрабатывает случаи, когда повторяющиеся слова находятся на разных строках,
как в предыдущем примере. Имя файла для анализа должно быть передано программе в качестве единственного аргумента
командной строки. При отсутствии аргумента или невозможности открыть указанный файл на экране
должно появляться соответствующее сообщение об ошибке.
"""
import sys
from Ex117 import *
def repeat_words(file_name):
    try:
        with open(file_name,  'r', encoding='utf-8') as readfile:
            words_set = set()
            count_line = 0
            for line in readfile:
                count_line += 1
                update_line = word(line)
                for w in update_line:
                    w = w.lower()
                    if w in words_set:
                        print(f'Найден повтор! Номер строки - ({count_line}), дублирующееся слово - {w}')
                    else:
                        words_set.add(w)

    except FileNotFoundError:
        print(f'Ошибка: файл ({file_name} не найден!)')

def main():
    if len(sys.argv) != 2:
        print("Ошибка: не указано имя файла.")
        quit()
    else:
        file_name = sys.argv[1]
        repeat_words(file_name)
if __name__ == '__main__':
    main()