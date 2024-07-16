"""
Упражнение 171. Строки фиксированной длины.
Напишите программу, которая будет открывать файл и выводить его на экран с постоянной длиной строк.
Если в исходном файле строка оказывается слишком длинной, «лишние» слова должны быть перенесены на следующую строку,
а если слишком короткой, слова со следующей строки должны перекочевать в конец текущей до полного ее заполнения.
Убедитесь, что ваша программа корректно обрабатывает тексты, в которых присутствуют абзацы.
Идентифицировать конец одного абзаца и начало другого можно по наличию пустой строки в
тексте после удаления символа конца строки.
"""

#  Функция format_paragraph принимает абзац текста и максимальную ширину строки.
#  Она разбивает абзац на слова и формирует строки заданной длины.
def format_paragraph(paragraph, max_width):
    # Разбиваем абзац на слова
    words = paragraph.split()
    formatted_lines = []
    current_line = []

    for word in words:
        # Проверяем, помещается ли текущее слово в текущую строку
        if sum(len(w) for w in current_line) + len(current_line) + len(word) <= max_width:
            current_line.append(word)
        else:
            # Если не помещается, добавляем текущую строку в список и начинаем новую строку
            formatted_lines.append(' '.join(current_line))
            current_line = [word]

    # Добавляем последнюю строку, если она не пустая
    if current_line:
        formatted_lines.append(' '.join(current_line))

    return formatted_lines

#  Функция format_file открывает файл, читает его строки и обрабатывает их,
#  склеивая строки абзацев и разделяя их пустыми строками.
#  Затем она передает каждый абзац в функцию format_paragraph для форматирования.
def format_file(filename, max_width=50):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            lines = file.readlines()

        formatted_text = []
        paragraph = []

        for line in lines:
            stripped_line = line.strip()
            if not stripped_line:
                # Если строка пустая, это конец абзаца
                if paragraph:
                    formatted_text.extend(format_paragraph(' '.join(paragraph), max_width))
                    formatted_text.append('')  # добавление пустой строки для разделения абзацев
                    paragraph = []
            else:
                # Добавляем строку к текущему абзацу
                paragraph.append(stripped_line)

        # Обрабатываем последний абзац, если он существует
        if paragraph:
            formatted_text.extend(format_paragraph(' '.join(paragraph), max_width))

        # Выводим отформатированный текст
        for formatted_line in formatted_text:
            print(formatted_line)

    except FileNotFoundError:
        print(f'Файл {filename} не найден.')
    except Exception as e:
        print(f'Ошибка при обработке файла {filename}: {e}')


filename = 'Ex162.txt'
max_width = 50
format_file(filename, max_width)