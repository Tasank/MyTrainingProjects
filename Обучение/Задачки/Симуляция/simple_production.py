from random import choice

def deposit(count):
    """
    Функция, имитирующая добычу ресурсов.
    Возвращает количество ресурсов и случайный тип ресурса.
    """
    name_set = ['Уголь', 'Камень', 'дерево', 'Песок']
    return count, choice(name_set)

class Fabric:
    """
    Класс, описывающий фабрику.
    """
    def __init__(self, name, work_time):
        """
        Инициализация фабрики.
        :param name: Название фабрики.
        :param work_time: Время работы фабрики.
        """
        self.name = name
        self.work_time = work_time
        self.product = 0

    def produce(self, quantity):
        """
        Производство продукции на фабрике.
        :param quantity: Количество продукции для производства.
        """
        self.product += quantity
        # Предполагаем, что каждая единица продукции занимает 5 единиц времени
        self.work_time -= 5 * quantity
        return self.work_time

    def __str__(self):
        """
        Возвращает строковое представление фабрики.
        """
        return f'Фабрика {self.name}, произведено: {self.product}'

def player(simulation_time):
    """
    Функция, имитирующая игрока.
    :param simulation_time: Время симуляции.
    :return: Количество добытых ресурсов.
    """
    mining_speed = 1
    extracted_resource = 0
    n = 1
    object_fabric_list = []

    count, name_deposit = deposit(1000)

    for current_time in range(simulation_time):
        extracted_resource += mining_speed

        if extracted_resource >= 50:
            extracted_resource = 0
            new_fabric = Fabric(f'Фабрика_{n}', simulation_time - current_time)
            # Передаем оставшееся время симуляции
            object_fabric_list.append(new_fabric)
            n += 1

        for fabric in object_fabric_list:
            if fabric.work_time > 0:
                fabric.produce(1)  # Производим 1 единицу продукции

    for fabric in object_fabric_list:
        print(fabric)

    return mining_speed * simulation_time

def play():
    """
    Основная функция.
    """
    while True:
        try:
            time = int(input('Введите количество минут симуляции: '))
            if time <= 0:
                print("Пожалуйста, введите положительное целое число.")
            else:
                break
        except ValueError:
            print("Пожалуйста, введите целое число.")

    player(time)

play()
