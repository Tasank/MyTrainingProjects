"""
Упражнение 95. Озаглавим буквы.
Многие в своих сообщениях не ставят заглавные буквы, особенно если используют для набора мобильные устройства.
Создайте функцию, которая будет принимать на вход исходную строку и
возвращать строку с восстановленными заглавными буквами.
"""
def format_text(text):
    new_text = ''
    capitalize_next = True
    for i in range(len(text)):
        if capitalize_next:
            if text[i] == ' ':
                continue
            else:
                new_text += " " + text[i].upper()

            capitalize_next = False
        else:
            new_text += text[i]
        if text[i] == '.' or text[i] == '!' or text[i] =='?':
            capitalize_next = True

    # Проверяем английски ли текст
    english_text = False
    if any(ord(char) > 127 for char in text):
        english_text = True
    if english_text:
        new_text = new_text.replace(' i ', ' I ')
        new_text = new_text.replace(' i.', ' I.')
        new_text = new_text.replace(' i!', ' I!')
        new_text = new_text.replace(' i?', ' I?')
    return new_text

def display():
    print('Программа поставит за вас заглавные буквы.')
    text = input('Введите текст: ')
    print(format_text(text))
display()