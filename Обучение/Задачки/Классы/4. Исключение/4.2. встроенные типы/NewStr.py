"""
Создайте новый класс NewStr, который наследуется от str. Добавьте метод reverse_words,
который позволяет развернуть слова в строке в обратном порядке.
"""

class NewStr(str):
    def revere_words(self):
        # return self[::-1]
        return " ".join(reversed(self.split()))

text = NewStr("Hello, World!")
print(text.revere_words())