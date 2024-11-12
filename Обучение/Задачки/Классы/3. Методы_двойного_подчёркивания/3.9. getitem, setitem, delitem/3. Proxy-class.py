"""
Создайте класс ProxyList, который является прокси-классом для списка.
Реализуйте методы __getitem__, __setitem__ и __delitem__,
чтобы можно было работать с элементами списка через прокси-класс.
"""


class ProxyList:
    def __init__(self, initial_list):
        self._list = initial_list if initial_list is not None else []

    def __getitem__(self, index):
        return self._list[index]

    def __setitem__(self, key, value):
        self._list[key] = value

    def __delitem__(self, key):
        del self._list[key]

    def __len__(self):
        return len(self._list)

    def append(self, element):
        self._list.append(element)

    def __repr__(self):
        return repr(self._list)


# Пример использования
proxy_list = ProxyList([1, 2, 3])
print(proxy_list[0])  # выведет 1

proxy_list[1] = 10
print(proxy_list[1])  # выведет 10

del proxy_list[2]
print(proxy_list)  # выведет [1, 10]
