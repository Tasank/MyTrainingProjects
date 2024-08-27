"""
Строки нужно сравнивать по количеству входящих в них символов.
Сравнивать между собой можно как объекты класса, так и обычные строки с экземплярами класса RealString.
Только 3 метода внутри класса (включая __init__()) для воплощения задуманного.
"""
from functools import total_ordering

# упрощает реализацию сравнений. Требует лишь 2 дополняющих варианта сравнения - например, больше и равно
@total_ordering
class RealString:
    def __init__(self, some_str):
        self.some_str = str(some_str)

    def __eq__(self, other):
        if not isinstance(other, RealString):
            other = RealString(other)

        return len(self.some_str) == len(other.some_str)

    def __lt__(self, other):
        if not isinstance(other, RealString):
            other = RealString(other)

        return len(self.some_str) < len(other.some_str)

str1 = RealString('десять')
str2 = RealString('десять и один.')
str3 = 'один'
str4 = [1, 2, 3]
print(str1 < str4)
print(str1 >= str2)
print(str1 == str3)
