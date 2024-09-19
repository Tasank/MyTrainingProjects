from random import choice
class Phone:
    def __init__(self, brand=None, model=None, price=None):
        self.brand = self.validate_brand(brand)
        self.model = self.validate_model(model)
        self.price = self.validate_price(price)

    def validate_model(self, model):
        if not model:
            model = ['X', '11', '12', '13']
            return choice(model)
        else:
            return model

    def validate_price(self, price):
        if not price:
            price = [1000, 2000, 3000, 4000]
            return choice(price)
        else:
            return price

    def validate_brand(self, brand):
        if not brand:
            brand = ['Apple', 'Samsung', 'Xiaomi', 'Huawei']
            return choice(brand)
        else:
            return brand
    def __str__(self):
        return f'Модель: {self.model}, цена: {self.price}, бренд: {self.brand}'

    def __repr__(self):
        return f'Объект класса: Phone, Атрибуты: brand=None, model=None, price=None'

my_phone = Phone()

print(my_phone)
print(repr(my_phone))
