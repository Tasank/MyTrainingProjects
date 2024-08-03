"""
Упражнение 182. Слова через химические элементы.
Напишите рекурсивную функцию, способную определять, можно ли выразить переданное ей слово исключительно через
обозначения химических элементов. Ваша функция должна принимать два параметра: слово, которое нужно проверить, и
список символов, которые можно при этом использовать. Возвращать функция должна строку, состоящую из использованных
символов, если собрать искомое слово можно, и пустую строку в противном случае. При этом регистры символов учитываться
не должны.
В основной программе должна быть использована ваша функция для проверки всех элементов таблицы
Менделеева на возможность составить их названия из обозначений химических элементов. Отобразите на экране названия элементов вместе с обозначениями, которые были использованы для их написания.
"""

# Список химических элементов и их символов
elements = [
    "H", "He", "Li", "Be", "B", "C", "N", "O", "F", "Ne",
    "Na", "Mg", "Al", "Si", "P", "S", "Cl", "Ar", "K", "Ca",
    "Sc", "Ti", "V", "Cr", "Mn", "Fe", "Co", "Ni", "Cu", "Zn",
    "Ga", "Ge", "As", "Se", "Br", "Kr", "Rb", "Sr", "Y", "Zr",
    "Nb", "Mo", "Tc", "Ru", "Rh", "Pd", "Ag", "Cd", "In", "Sn",
    "Sb", "Te", "I", "Xe", "Cs", "Ba", "La", "Ce", "Pr", "Nd",
    "Pm", "Sm", "Eu", "Gd", "Tb", "Dy", "Ho", "Er", "Tm", "Yb",
    "Lu", "Hf", "Ta", "W", "Re", "Os", "Ir", "Pt", "Au", "Hg",
    "Tl", "Pb", "Bi", "Po", "At", "Rn", "Fr", "Ra", "Ac", "Th",
    "Pa", "U", "Np", "Pu", "Am", "Cm", "Bk", "Cf", "Es", "Fm",
    "Md", "No", "Lr", "Rf", "Db", "Sg", "Bh", "Hs", "Mt", "Ds",
    "Rg", "Cn", "Nh", "Fl", "Mc", "Lv", "Ts", "Og"
]

"Внешняя функция принимает два параметра слово и список хим. элементов."
def can_spell(word, elements):
    # Приводим слово и элементы к нижнему регистру для удобства сравнения
    word = word.lower()
    elements = [e.lower() for e in elements]
    "Внутренняя рекурсивная функция пытается найти элемент с которого начинается слово"
    def helper(word):
        if not word:
            return ""
        for el in elements:
            # startswith проверяет, начинается ли строка с подстроки(элемента)
            if word.startswith(el):
                # Рекурсивный вызов с оставшейся частью слова:
                # Если word начинается с el, то функция helper вызывается рекурсивно с оставшейся частью слова
                result = helper(word[len(el):])
                # Если рекурсивный вызов успешен (не вернул None), то текущий элемент добавляется к результату
                if result is not None:
                    return el.capitalize() + result
        return None

    return helper(word)

def main():
    """Тестовые слова для проверки"""
    # elements_to_check = [
    #     "Hydrogen", "Helium", "Lithium", "Beryllium", "Boron", "Carbon",
    #     "Nitrogen", "Oxygen", "Fluorine", "Neon", "Sodium", "Magnesium",
    #     "Aluminum", "Silicon", "Phosphorus", "Sulfur", "Chlorine",
    #     "Argon", "Potassium", "Calcium", "Scandium", "Titanium",
    #     "Vanadium", "Chromium", "Manganese", "Iron", "Cobalt",
    #     "Nickel", "Copper", "Zinc", "Gallium", "Germanium", "Arsenic",
    #     "Selenium", "Bromine", "Krypton", "Rubidium", "Strontium",
    #     "Yttrium", "Zirconium", "Niobium", "Molybdenum", "Technetium",
    #     "Ruthenium", "Rhodium", "Palladium", "Silver", "Cadmium",
    #     "Indium", "Tin", "Antimony", "Tellurium", "Iodine", "Xenon",
    #     "Cesium", "Barium", "Lanthanum", "Cerium", "Praseodymium",
    #     "Neodymium", "Promethium", "Samarium", "Europium", "Gadolinium",
    #     "Terbium", "Dysprosium", "Holmium", "Erbium", "Thulium",
    #     "Ytterbium", "Lutetium", "Hafnium", "Tantalum", "Tungsten",
    #     "Rhenium", "Osmium", "Iridium", "Platinum", "Gold", "Mercury",
    #     "Thallium", "Lead", "Bismuth", "Polonium", "Astatine", "Radon",
    #     "Francium", "Radium", "Actinium", "Thorium", "Protactinium",
    #     "Uranium", "Neptunium", "Plutonium", "Americium", "Curium",
    #     "Berkelium", "Californium", "Einsteinium", "Fermium", "Mendelevium",
    #     "Nobelium", "Lawrencium", "Rutherfordium", "Dubnium", "Seaborgium",
    #     "Bohrium", "Hassium", "Meitnerium", "Darmstadtium", "Roentgenium",
    #     "Copernicium", "Nihonium", "Flerovium", "Moscovium", "Livermorium",
    #     "Tennessine", "Oganesson"
    # ]
    """Проверка слов без ввода пользователя"""
    # for element in elements_to_check:
    #     result = can_spell(element, elements)
    #     if result:
    #         print(f"{element} может быть представлен как {result}")
    #     else:
    #         print(f"{element} не может быть представлен через химические элементы")

    to_check = input('Введите слово: ')
    result = can_spell(to_check, elements)

    if result:
        print(f"{to_check} может быть представлен как {result}")
    else:
        print(f"{to_check} не может быть представлен через химические элементы")


if __name__ == "__main__":
    main()
