class IProduct:
    def get_price(self):
        pass


class Product(IProduct):
    def __init__(self, name, price):
        self._name = name
        self._price = price

    def get_price(self):
        return self._price


class IOrder:
    def add_product(self, product):
        pass

    def get_total_price(self):
        pass


class Order(IOrder):
    def __init__(self):
        self._products = []

    def add_product(self, product):
        self._products.append(product)

    def get_total_price(self):
        return sum(product.get_price() for product in self._products)


class ICustomer:
    def get_name(self):
        pass

    def set_name(self, name):
        pass


class Customer(ICustomer):
    def __init__(self, name):
        self._name = name

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name


class IShipper:
    def ship_order(self, order, customer):
        pass


class Shipper(IShipper):
    def ship_order(self, order, customer):
        print(f'Shipping order of total price {order.get_total_price()} to customer {customer.get_name()}')


def test_srp_and_ocp():
    product1 = Product('product1', 10)
    product2 = Product('product2', 20)
    order = Order()
    order.add_product(product1)
    order.add_product(product2)
    assert order.get_total_price() == 30


def test_lsp():
    product1 = Product('product1', 10)
    order = Order()
    order.add_product(product1)
    assert isinstance(order, IOrder)


def test_isp():
    customer = Customer('customer1')
    shipper = Shipper()
    order = Order()
    product1 = Product('product1', 10)
    order.add_product(product1)
    shipper.ship_order(order, customer)
    assert isinstance(shipper, IShipper)


def test_dip():
    customer = Customer('customer1')
    order = Order()
    product1 = Product('product1', 10)
    order.add_product(product1)
    shipper = Shipper()
    shipper.ship_order(order, customer)
    assert isinstance(customer, ICustomer)
    assert isinstance(order, IOrder)
    assert isinstance(product1, IProduct)


test_srp_and_ocp()
test_lsp()
test_isp()
test_dip()
