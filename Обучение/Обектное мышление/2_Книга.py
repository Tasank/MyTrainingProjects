class Book:
    def __init__(self, title: str, author: str, num_pages: int, material: str, pages: dict):
        self.title = title
        self.author = author
        self.num_pages = num_pages
        self.pages = pages
        self.material = self.check_material(material)


    def check_material(self, material):
        tup_material = ('Бумажная основа', 'Тканевая основа', 'Не тканевая основа')
        if material in tup_material:
            return material
        else:
            return tup_material[0]


    def read(self):
        try:
            print(f'Всего страниц: {len(self.pages.keys())}')
            n = int(input('Введите номер страницы чтобы начать чтение: '))

            if n not in self.pages.keys():
                print('[ПРЕДУПРЕЖДЕНИЕ] Такого номера страницы нет.\n')
                return self.read()
        except ValueError:
            print('[ПРЕДУПРЕЖДЕНИЕ] Введите номер (число) страницы.\n')
            return self.read()

        def rec_read(n=0):
            if n == len(self.pages.keys()):
                print('Книга прочитана!')
                return
            else:
                print('-' * 50)
                print(f'\n\n{n} из {len(self.pages.keys())} страниц.')
                print(f'{self.pages[n]}\n\n')  # Доделать вывод в кол-во символов в строке
                print('-' * 50)
                next_r = input('Для продолжения чтения нажмите Enter.\nЧтобы завершить чтение напишите "закрыть": ')
                if next_r.lower() == 'закрыть':
                    return
                n += 1
                return rec_read(n)
        rec_read(n)





    def info(self):
        print(self)  # Придумать вывод названия объекта
        print(f'Название: {self.title}\n'
              f'Автор: {self.author}\n'
              f'Количество страниц в книге: {self.num_pages}\n'
              f'Материал: {self.material}\n\n'
              )


book = Book('Сайрус', "Михаил Янченко",
            346, "gh",
            {1: 'Содержание первой страницы', 2: "Содержание второй страницы"})

book_1 = Book('Советские сказки', "Александр Остапов",
            222, "Тканевая основа",
            {1: 'Содержание первой страницы', 2: "Содержание второй страницы"})
book.info()
book_1.info()
book.read()
