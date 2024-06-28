"""
Упражнение 159. Случайный пароль из двух слов.
Напишите программу, которая будет открывать файл со списком слов, случайным образом выбирать
два из них и сцеплять вместе для получения итогового пароля. При создании пароля исходите из следующего требования:
он должен состоять минимум из восьми символов и максимум из десяти, а каждое из используемых слов должно быть
длиной хотя бы в три буквы. Кроме того, сделайте заглавными первые буквы обоих слов, чтобы легко можно было понять,
где заканчивается одно и начинается другое. По завершении процесса полученный пароль должен быть отображен на экране.
"""
from random import choice

# Отдельная функция для генерации пароля
def generate_password(word_list):
    count = 0
    while True:
        count += 1
        if count == 1000:
            return 'В файле нет слов, подходящих для создания пароля'
        # title() делает первую букву слова заглавной
        first_word = choice(word_list).title()
        second_word = choice(word_list).title()

        if len(first_word) >= 3 or len(second_word) >= 3:
            total_word = first_word + second_word
            if 8 <= len(total_word) <= 10:
                return total_word

def main():
    filename = input('Введите имя файла слов: ')
    try:
        # Если файл txt с русскими словами добавляем encoding='utf-8'
        with open(filename, 'r', encoding='utf-8') as readfile:
            word_list = readfile.read().split()
            print(generate_password(word_list))
    except FileNotFoundError:
        print('Файл не найден.')

if __name__ == '__main__':
    main()