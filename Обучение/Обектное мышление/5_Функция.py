class Function:
    def __init__(self, task_type):
        self.task_type = task_type

    def __call__(self, *args, **kwargs):
        if self.task_type == 'вывод':
            self._print_function(*args, **kwargs)
        elif self.task_type == 'сумма':
            return self._sum_function(*args, **kwargs)
        elif self.task_type == 'ввод':
            return self._input_function(*args, **kwargs)
        else:
            raise ValueError(f'Недопустимый тип задачи: {self.task_type}')

    def _print_function(self, message):
        print(f'Вывод: {message}')

    def _sum_function(self,arg1, arg2):
        return arg1 + arg2

    def _input_function(self, message):
        return f'Зарегистрировано: {input(message)}'



f = Function('вывод')
f('Вывод сообщения.')

s = Function('сумма')
sum_num = s(1, 2)
print(sum_num)


f = Function('ввод')
print(f('Введи свое имя: '))
