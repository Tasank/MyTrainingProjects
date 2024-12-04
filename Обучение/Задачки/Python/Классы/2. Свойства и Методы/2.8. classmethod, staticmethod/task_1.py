
class MyClass:
    text = 'Это атрибут класса.'
    @classmethod
    def info_cls(cls):
        print(f'Это  метод класса. Я могу использовать (cls.text): ({cls.text})')

    @staticmethod
    def info_static():
        print(f'Это статический метод. Который не имеет доступа к классу или его атрибутам')
        print(f'Я не могу использовать (self.text) но могу делать так (MyClass.text) - ({MyClass.text})')


MyClass.info_cls()
MyClass.info_static()
