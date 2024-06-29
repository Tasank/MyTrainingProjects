"""
Упражнение 161. Что за химический элемент?
Напишите программу, которая будет считывать файл, содержащий информацию о химических элементах,
и сохранять ее в более подходящей для этого структуре данных. После этого пользователь должен ввести значение.
Если введенное значение окажется целочисленным, программа должна вывести на экран обозначение и название химического
элемента с введенным количеством протонов. При вводе пользователем строки необходимо отобразить количество
протонов элемента с введенным пользователем обозначением или названием.
Если введенное пользователем значение не соответствует ни одному из элементов в файле,
необходимо вывести соответствующее сообщение об ошибке.
Позвольте пользователю вводить значения до тех пор, пока он не оставит ввод пустым.
"""

def read_elements():
    elements_protons = {}
    elements_symbols = {}
    elements_name = {}

    with open('Ex161.txt', 'r') as readfile:
        for line in readfile:
            content = line.strip().split(',')
            # Инициализация переменных
            protons = int(content[0])
            symbols = content[1]
            name = content[2]
            # Добавление в подходящие структуры данных
            elements_protons[protons] = (symbols, name)
            elements_symbols[symbols] = protons
            elements_name[name] = (symbols, protons)
    return elements_protons, elements_symbols, elements_name

def main():
    elements_protons, elements_symbols, elements_name = read_elements()
    try:
        while True:
            ask = input("Введите количество протонов, обозначение или название элемента: ").strip()

            if not ask:
                break
            # Если введенное значение окажется целочисленным
            if ask.isdigit():
                protons = int(ask)
                if protons in elements_protons:
                    symbol, name = elements_protons[protons]
                    print(f'{symbol},{name}')
                else:
                    print('Нет элемента с таким номером.')
            else:
                # Найти значение по ключу в словаре протонов или словаре имён
                protons = elements_symbols.get(ask) or elements_name.get(ask.lower())
                if protons:
                    print(f"Количество протонов: {protons}")
                else:
                    print("Ошибка: элемент не найден")
    except KeyboardInterrupt:
        print('Завершение программы.')
        quit()

if __name__ == '__main__':
    main()