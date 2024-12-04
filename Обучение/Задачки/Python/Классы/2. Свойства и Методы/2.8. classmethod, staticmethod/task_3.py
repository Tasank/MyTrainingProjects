"""
2. Создайте класс `String` с staticmethod `reverse`, который принимает строку и возвращает ее в обратном порядке.
"""

class String:
    @staticmethod
    def reverse(text):
        return text[::-1]

print(f'{String.reverse("Переверни меня")}') # янем инревереП

text = String()
print(f'{text.reverse("Сделай это снова")}') # авонс отэ йаледС
