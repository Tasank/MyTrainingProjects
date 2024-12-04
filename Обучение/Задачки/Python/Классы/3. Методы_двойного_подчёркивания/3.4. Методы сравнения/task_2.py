"""
Определите класс Book с атрибутами title, author и year, которые представляют собой название,
автора и год издания книги. Переопределите методы __eq__ и __gt__, чтобы определить,
когда две книги равны и когда одна книга была издана позже другой.

Например, если у вас есть две книги b1 = Book("Книга1", "Автор1", 2000) и b2 = Book("Книга1", "Автор1", 2000),
то b1 == b2 должно вернуть True, а b1 > b2 должно вернуть False. Если у вас есть две книги
b1 = Book("Книга1", "Автор1", 2000) и b2 = Book("Книга2", "Автор2", 2005), то b1 > b2 должно вернуть False.
"""

class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    # Переопределение (=)
    def __eq__(self, other):
        if isinstance(other, Book):
            return self.title == other.title and self.author == other.author and self.year == other.year
        return False

    # Переопределение (>)
    def __gt__(self, other):
        if isinstance(other, Book):
            return self.year > other.year
        return False


b1 = Book("Книга_1", "Автор_1", 2000)
b2 = Book("Книга_1", "Автор_1", 2000)
b3 = Book("Книга_2", "Автор_2", 2005)

print(b1 == b2)
print(b1 == b3)
print(b1 > b2)
print(b1 > b3)
print(b3 > b2)