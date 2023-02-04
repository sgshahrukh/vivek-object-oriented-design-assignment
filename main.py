class IProduct:
    def get_price(self):
        pass


class Product(IProduct):
    def __init__(self, name, price):
        self._name = name
        self._price = price

    def get_price(self):
        return self._price



