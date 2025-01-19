def console():
    variables = {}

    def info():
        print('Это имитация программирования в консоли.')
        print('--------Основные команды--------')
        print('Помощь - выводит список команд')
        print('Выход - завершает программу   ')
        print('Ввод - запускает функцию, которую нужно написать')
        print('---------------------------------\n\n')
        print('Доступные команды (Ввод): ')
        print('(Присвоить) - присвоить переменной значение')
        print('Например: Присвоить a 4, Присвоить b 5\n')
        print('(Сложить) - сложить две переменные')
        print('Например: Сложить a b\n')
        print('---------------------------------\n\n')

    def command(text):
        if text == 'Помощь':
            info()
        elif text == 'Выход':
            print('Завершение программы...')
            exit()
        elif text == 'Ввод':
            task = input('Ввод: ').split()
            if task[0] == 'Присвоить' and len(task) == 3:
                variable = task[1]
                try:
                    value = int(task[2])
                    variables[variable] = value
                    print(f'Переменной {variable} присвоено значение {value}')
                except ValueError:
                    print('Ошибка: значение должно быть числом.')

            elif task[0] == 'Сложить' and len(task) == 3:
                var1 = task[1]
                var2 = task[2]
                if var1 in variables and var2 in variables:
                    result = variables[var1] + variables[var2]
                    print(f'Результат сложения {var1} и {var2}: {result}')
                else:
                    print('Ошибка: одна или обе переменные не найдены.')
            else:
                print('Неверная команда или параметры.')

    def main():
        info()
        while True:
            command(input('Введите команду: '))

    main()


console()
