"""
Упражнение 169. Редактирование текста в файле.
В данном упражнении вам необходимо написать программу, которая будет заменять все служебные слова в
тексте на символы звездочек (по количеству символов в словах).
Вы должны осуществлять регистрозависимый поиск служебных слов в тексте,
даже если эти слова входят в состав других слов.
Список служебных слов должен храниться в отдельном файле.
Сохраните отредактированную версию исходного файла в новом файле.
Имена исходного файла, файла со служебными словами и нового файла должны быть введены пользователем.
"""
def replace_keywords_in_file(source_file, keywords_file, output_file, case_sensitive='нет'):
    try:
        # Чтение служебных слов
        with open(keywords_file, 'r', encoding='utf-8') as read_key_f:
            keywords = [line.strip() for line in read_key_f.readlines()]

        # Чтение исходного файла
        with open(source_file, 'r', encoding='utf-8') as read_sour_f:
            content = read_sour_f.read()

        if case_sensitive == 'да':
            print('Внимание! Весь текст будет приведён к нижнему регистру.')

        #Замена служебных слов на звездочки
        for keyword in keywords:
            replacement = '*' * len(keyword)
            if case_sensitive == 'да':
                keyword = keyword.lower()
                content = content.lower()
                content = content.replace(keyword, replacement)

            else:
                content = content.replace(keyword, replacement)



        # Запись в выходной файл
        with open(output_file, 'w', encoding='utf-8') as of:
            of.write(content)

        print(f'Файл успешно обработан и сохранен как {output_file}')

    except FileNotFoundError as e:
        print(f'Ошибка: файл не найден - {e.filename}')

def main():
    ask = input('Использовать исходные файлы? (да/нет): ').lower()
    if ask == 'да':
        source_file = 'Ex169_source.txt'
        keywords_file = 'Ex169_keywords.txt'
        output_file = 'Ex169_total.txt'
    else:
        source_file = input('Введите имя исходного файла: ')
        keywords_file = input('Введите имя файла со служебными словами: ')
        output_file = input('Введите имя выходного файла: ')

    case_sensitive = input('Учитывать регистр? (да/нет): ').strip().lower()

    replace_keywords_in_file(source_file, keywords_file, output_file, case_sensitive)

if __name__ == '__main__':
    main()