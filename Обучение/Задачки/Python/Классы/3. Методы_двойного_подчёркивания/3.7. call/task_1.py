class Pandora_Box:
    def __init__(self):
        self.counter = 0
        self.value = 0

    @staticmethod
    def info():
        print('Ключ-слово: "Открыть"')
        print('Ключ-слово: "Узнать"', end='\n\n')

    info()

    def __call__(self, ask):
        self.counter += 1
        if ask == 'Открыть':
            print('Открываем пандору. Обнуление.')
        elif ask == 'Узнать':
            print(f'Текущая вероятность: {self.value:.2f}')
            print(f'Количество внимания: {self.counter}')
        else:
            self.value += 0.01

        if self.value == 1:
            print('Пандора открылась волей случая! Обнуление.')
            self.counter = 0
            self.value = 0

p = Pandora_Box()
p('Открыть')
p('')
p('Узнать')
