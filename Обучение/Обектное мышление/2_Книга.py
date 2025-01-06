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