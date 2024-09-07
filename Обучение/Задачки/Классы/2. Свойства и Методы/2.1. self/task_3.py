"""
В классах ООП self используется для обращения к атрибутам и
методам экземпляра класса. Это позволяет методам класса
взаимодействовать с конкретным экземпляром класса, а не с классом в целом.
"""

class Action:
    act = 'Ломать'
    def play_action(*args):
        """
        Метод класса, который принимает любое количество аргументов,
        в этом методе не используется self, поэтому он не может обращаться к атрибутам или методам экземпляра класса.
        :param args:
        :return:
        """
        print('Применено к -', args, '\n')

    def show_attribute(self):
        print(f'Мои атрибуты: {self.act} \n')

    def create_attribute(self):
        self.refund = 'Создать'
        print(f'Мы создали атрибут: {self.act} \n')

play = Action()

play.play_action('коробку')
play.show_attribute()
play.create_attribute()