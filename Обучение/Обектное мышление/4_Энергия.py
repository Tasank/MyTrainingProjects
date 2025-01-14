
class Energy:
    def __init__(self, value: int, unit: str):
        self.value = value
        self.unit = unit

    def add_energy(self, energy_to_add: int):
        try:
            self.value += energy_to_add
            return f'Добавлено: {energy_to_add} энергии.'
        except Exception as e:
            return f'Произошла ошибка: {e}'

    def consume_energy(self, energy_to_consume: int):
        try:
            if self.value > energy_to_consume:
                self.value -= energy_to_consume
                return f'Ушло: {energy_to_consume} энергии.'
            else:
                print(f'Потребляемая энергия ({energy_to_consume}) больше наличии энергии ({self.value})\n'
                      f'Текущее значение: 0')
                self.value = 0
                return ''
        except Exception as e:
            return f'Произошла ошибка: {e}'


N1 = Energy(10, 'Ньютонов')
N1.add_energy(19)
print(N1.add_energy('d'))

print(N1.consume_energy(220))