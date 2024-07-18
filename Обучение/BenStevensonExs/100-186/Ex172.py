"""
Упражнение 172. Слова с шестью гласными в ряд.
Существует как минимум одно слово в английском языке, содержащее все гласные буквы в том порядке,
в котором они расположены в алфавите, а именно A, E, I, O, U и Y.
Напишите программу, которая будет просматривать текстовый файл на предмет поиска и отображения таких слов.
Имя исходного файла должно быть запрошено у пользователя.
Если имя файла окажется неверным или возникнут иные ошибки при чтении файла,
выведите соответствующее сообщение об ошибке.
"""

def open_file(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            words = file.read().strip().split()

        target_sequence = "aeiouy"
        result = []

        # Проходим по каждому слову в тексте
        for word in words:
            # Извлекаем гласные в слове, если они находятся в целевой последовательности
            vowels_in_word = ''.join([char for char in word if char.lower() in target_sequence])
            # Проверяем, совпадает ли последовательность гласных с целевой
            if vowels_in_word == target_sequence:
                result.append(word)

        if result:
            print(f'Слова с шестью гласными в ряд: {", ".join(result)}')
        else:
            print("Нет слов с шестью гласными в указанном порядке.")

    except FileNotFoundError:
        print(f'Файл {filename} не найден.')
    except Exception as e:
        print(f'Произошла ошибка: {e}')

# Запрашиваем у пользователя имя файла
# Ex172.txt
filename = input("Введите имя файла: ")
open_file(filename)
