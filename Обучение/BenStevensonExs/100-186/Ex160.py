"""
Упражнение 160. Странные слова.
Напишите программу, которая будет построчно обрабатывать текстовый файл.
В каждой строке может присутствовать много слов, а может и не быть ни одного.
Слова, в которых буквы E и I не соседствуют друг с другом, обработке подвергать не следует.
Если же такое соседство присутствует, необходимо проверить, соответствует ли написание анализируемого
слова указанному выше правилу. Создайте и выведите на экран два списка. В первом должны располагаться слова,
следующие правилу, а во втором – нарушающие его. При этом списки не должны содержать повторяющиеся слова.
Также отобразите на экране длину каждого списка, чтобы пользователю было понятно,
сколько слов в файле не отвечает правилу.
"""

def check_word(word_list):
    # Множество для хранения слов без повторений
    correct_list = set()
    wrong_list = set()
    for word in word_list:
        # Проверка на наличие последовательностей 'ei' или 'ie' в слове
        if 'ei' in word or 'ie' in word:
            if 'cei' in word:
                correct_list.add(word)
            elif 'cie' in word:
                wrong_list.add(word)
            # Проверяем, если слово содержит 'ie' и не содержит 'cie', то оно правильное
            elif 'ie' in word and 'cie' not in word:
                correct_list.add(word)
            elif 'ei' in word and 'cei' not in word:
                wrong_list.add(word)
    return list(correct_list), list(wrong_list)

def main():
    print('Правило «I before E except after C» ')
    try:
        with open('Ex160.txt', 'r', encoding='utf-8') as readfile:
            word_list = readfile.read().split()
            correct_list, wrong_list = check_word(word_list)
            print(f'Список следующие правилу {correct_list}')
            print('Его длинна: ', len(correct_list))
            print()
            print(f'Список нарушающие его {wrong_list}')
            print('Его длинна: ', len(wrong_list))
    except FileNotFoundError:
        print('Файл не найден')

if __name__ == '__main__':
    main()