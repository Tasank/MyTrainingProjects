"""
Упражнение 122. «Поросячья латынь».
Напишите программу, которая будет запрашивать у пользователя строку. После этого она должна переводить введенный текст
на «поросячью латынь» и выводить его на экран. Вы можете сделать допуск о том, что все слова пользователь будет вводить
в нижнем регистре и разделять их пробелами.
"""

def pig_latin(word):
    consonants = 'wrtpsdfghjklzxcvbnm'
    vowels = 'aieou'
    if word[0] in vowels:
        return word + 'way'
    elif word[0] in consonants:
        # enumerate возвращает индекс и значение
        for index, letter in enumerate(word):
            if letter in vowels:
                return word[index:] + word[:index] + 'ay'


def ask():
    line = input('Введите строку: ')
    word_list = line.split()
    # Генератор списка, чтобы применить функцию к каждому слову и создать новый список
    piglatin_list = [pig_latin(word) for word in word_list]
    print('Поросячья латынь -> ', *piglatin_list)

ask()