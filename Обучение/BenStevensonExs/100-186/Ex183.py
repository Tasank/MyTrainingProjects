"""
Упражнение 183. Последовательность химических элементов.
Напишите программу, которая будет запрашивать у пользователя химический элемент и при помощи рекурсивной функции
определять максимально возможную последовательность слов. Выведите на экран полученный ряд.
Удостоверьтесь, что программа выводит соответствующее сообщение об ошибке, если пользователь укажет
несуществующий химический элемент.
"""
import time
# список всех химических элементов и их обозначений
elements = [
    "Hydrogen", "Helium", "Lithium", "Beryllium", "Boron", "Carbon", "Nitrogen", "Oxygen", "Fluorine", "Neon",
    "Sodium", "Magnesium", "Aluminum", "Silicon", "Phosphorus", "Sulfur", "Chlorine", "Argon", "Potassium", "Calcium",
    "Scandium", "Titanium", "Vanadium", "Chromium", "Manganese", "Iron", "Cobalt", "Nickel", "Copper", "Zinc",
    "Gallium", "Germanium", "Arsenic", "Selenium", "Bromine", "Krypton", "Rubidium", "Strontium", "Yttrium", "Zirconium",
    "Niobium", "Molybdenum", "Technetium", "Ruthenium", "Rhodium", "Palladium", "Silver", "Cadmium", "Indium", "Tin",
    "Antimony", "Tellurium", "Iodine", "Xenon", "Cesium", "Barium", "Lanthanum", "Cerium", "Praseodymium", "Neodymium",
    "Promethium", "Samarium", "Europium", "Gadolinium", "Terbium", "Dysprosium", "Holmium", "Erbium", "Thulium", "Ytterbium",
    "Lutetium", "Hafnium", "Tantalum", "Tungsten", "Rhenium", "Osmium", "Iridium", "Platinum", "Gold", "Mercury",
    "Thallium", "Lead", "Bismuth", "Polonium", "Astatine", "Radon", "Francium", "Radium", "Actinium", "Thorium",
    "Protactinium", "Uranium", "Neptunium", "Plutonium", "Americium", "Curium", "Berkelium", "Californium", "Einsteinium", "Fermium",
    "Mendelevium", "Nobelium", "Lawrencium", "Rutherfordium", "Dubnium", "Seaborgium", "Bohrium", "Hassium", "Meitnerium", "Darmstadtium",
    "Roentgenium", "Copernicium", "Nihonium", "Flerovium", "Moscovium", "Livermorium", "Tennessine", "Oganesson"
]


def find_longest_chain(start_element, elements):
    #  рекурсивная функция find_chain, которая строит цепочку элементов
    def find_chain(current_element, chain):
        # Функция ищет возможные элементы, которые можно добавить к цепочке, и вызывает саму себя
        # для каждого такого элемента
        last_letter = current_element[-1].lower()
        possible_elements = [el for el in elements if el[0].lower() == last_letter and el not in chain]

        if not possible_elements:
            return chain

        longest_chain = chain

        for el in possible_elements:
            new_chain = find_chain(el, chain + [el])
            if len(new_chain) > len(longest_chain):
                longest_chain = new_chain

        return longest_chain

    if start_element not in elements:
        return "Ошибка: Некорректный элемент."

    chain = find_chain(start_element, [start_element])
    return chain

start_element = input("Введите химический элемент: ")

# Для подсчёта времени на такую операцию, запуск таймера
start_time = time.time()
result = find_longest_chain(start_element, elements)

# Остановка таймера
end_time = time.time()

# подсчёт времени
total_time = end_time - start_time

# Кол-во слов
count_words = 0
for word in result:
    count_words += 1
    print(word)
print(f'[Всего слов: {count_words}]')
print(f'[Время выполнения: {total_time:.2f} секунды]')