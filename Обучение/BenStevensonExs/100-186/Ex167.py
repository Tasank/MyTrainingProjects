"""
Упражнение 167. Проверяем правильность написания.
В данном упражнении мы напишем простую программу, сверяющую слова из текстового файла со словарем.
Неправильно написанными будем считать все слова, которых не нашлось в словаре.
"""
# Запуск python Ex167.py Ex167.txt
import sys
from Ex117 import word

# Словарь с правильными словами
dictionary = {
    "привет": True,
    "мир": True,
    "этот": True,
    "текст": True,
    "содержит": True,
    "некоторые": True,
    "слова": True,
    "которые": True,
    "могут": True,
    "быть": True,
    "написаны": True,
    "с": True,
    "ошибками": True,
    "например": True,
    "слово": True,
    "или": True,
    "проверка": True,
    "написана": True,
    "корректна": True,
    "не": True,
    "также": True,
    "что": True,
    "будут": True,
    "повторяться": True,
    "чтобы": True,
    "вы": True,
    "могли": True,
    "провести": True,
    "орфографическую": True,
    "на": True,
    "повторяющиеся": True
}

def check_text(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as readfile:
            # Используем функцию из Ex117 для обработки текста
            update_text_1 = word(readfile.read())
            for w in update_text_1:
                if w.lower() not in dictionary:
                    print(f'Слово ({w}) является неправильным!')
            print('Проверка завершена. Все неправильные слова не входят в словарь "правильных".')

    except FileNotFoundError:
        print(f'Ошибка: файл "{filename}" не найден.')

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Ошибка: не указано имя файла.")
        sys.exit(1)
    else:
        file_name = sys.argv[1]
        check_text(file_name)
