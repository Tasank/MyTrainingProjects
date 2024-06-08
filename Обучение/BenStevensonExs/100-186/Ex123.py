"""
Упражнение 123. «Поросячья латынь» (продолжение).
Расширьте свое решение упражнения 122, чтобы ваш анализатор корректно обрабатывал символы в верхнем регистре
и знаки препинания, такие как запятая, точка, а также восклицательный и вопросительный знаки.
Если в оригинале слово начинается с заглавной буквы, то в переводе на «поросячью латынь» оно также должно
начинаться с заглавной буквы, тогда как буквы, перенесенные в конец слов, должны стать строчными.
Если в конце слова стоит знак препинания, он там же и должен остаться после выполнения перевода.
То есть слово в конце предложения Science! необходимо трансформировать в Iencescay!.
"""

def pig_latin(word):
    # Объявление переменных
    vowels = 'aieou'
    signs = ['!', '.', ',', '?', ':', ';']

    punctuation = False
    up = False
    total_word = None
    word_end = None

    # Проверяем на наличие заглавной буквы
    if word[0].isupper():
        up = True
        word = word.lower()

    # Проверяем на наличие пунктуации
    if word[-1] in signs:
        punctuation = True
        word_end = word[-1]
        word = word[:-1]

    if word[0] in vowels:
        total_word = word + 'way'
    else:
        # enumerate возвращает индекс и значение
        for index, letter in enumerate(word):
            # Игнорируем "y"
            if letter in vowels or letter == 'y':
                total_word = word[index:] + word[:index] + 'ay'
                break

    # Проверяем была ли заглавная буква
    if punctuation:
        total_word += word_end
    if up:
        total_word = total_word.capitalize()

    return total_word

def ask():
    line = input('Введите строку: ')
    word_list = line.split()
    # Генератор списка, чтобы применить функцию к каждому слову и создать новый список
    piglatin_list = [pig_latin(word) for word in word_list]
    print('Поросячья латынь -> ', *piglatin_list)

ask()