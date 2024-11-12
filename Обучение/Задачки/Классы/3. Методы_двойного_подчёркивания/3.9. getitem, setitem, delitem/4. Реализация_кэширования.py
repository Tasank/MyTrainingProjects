"""
Создайте класс Cache, который хранит в себе данные в виде словаря.
Реализуйте методы __getitem__ и __setitem__,
чтобы данные хранились в кэше и при доступе к ним они не загружались заново.
"""

class Cache():
    def __init__(self):
        self.cache = {}

    def __getitem__(self, item):
        return self.cache[item]

    def __setitem__(self, key, value):
        self.cache[key] = value

    def __repr__(self):
        return repr(self.cache)

# Пример использования
cache = Cache()

cache["key"] = "value"
print(cache["key"])  # выведет "value"

cache["key"] = "new_value"
print(cache["key"])  # выведет "new_value"
