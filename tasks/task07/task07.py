import uuid
import time


class Good:
    def __init__(self, name, price):
        self.id = uuid.uuid4()
        self.name = name
        self.price = price


class Order:
    def __init__(self, client_id, goods):
        self.order_id = uuid.uuid4()
        self.order_date = time.time()
        self.goods = goods
        self.client_id = client_id

    @property
    def price(self):
        return sum(good.price for good in self.goods)


class Orders:
    __orders = {}

    def create(self, order):
        self.__orders.setdefault(order.order_id, order)

    def read(self, order_id):
        return self.__orders.get(order_id)

    def read_latest(self, n_latest):
        if len(self.__orders) == 0:
            return None

        order_items = [*self.__orders.values()]

        if n_latest is None:
            return order_items
        else:
            return order_items[-n_latest:]

    def update(self, order):
        if order.order_id in self.__orders:
            self.__orders[order.order_id] = order
        else:
            self.create(order)

    def delete(self, order_id):
        if order_id in self.__orders:
            del self.__orders[order_id]


class OrderRepository:
    def __init__(self, context):
        self.__context = context

    def add(self, order):
        self.__context.create(order)

    def get(self, order_id):
        return self.__context.read(order_id)

    def list(self, n_latest=None):
        return self.__context.read_latest(n_latest)

    def delete(self, order_id):
        return self.__context.delete(order_id)


apple = Good("Apple", 2)
pineapple = Good("Pineapple", 3)
lime = Good("Lime", 6)
potatoes = Good("Potatoes", 1)
strawberry = Good("Strawberry", 9)

client1_id = uuid.uuid4()
client2_id = uuid.uuid4()

client1_order = Order(client1_id, [apple, potatoes, lime])
client2_order = Order(client2_id, [pineapple, apple, strawberry])

order_repository = OrderRepository(Orders())

assert order_repository.list() == None

order_repository.add(client1_order)
order_repository.add(client2_order)

assert client1_order.price == 9
assert client2_order.price == 14
assert sum(orders.price for orders in order_repository.list()) == 23

assert order_repository.list() == [client1_order, client2_order]
assert order_repository.list(1) == [client2_order]
assert order_repository.get(client1_order.order_id) == client1_order

order_repository.delete(client1_order.order_id)
assert order_repository.list() == [client2_order]
assert order_repository.get(client1_order.order_id) == None
assert sum(orders.price for orders in order_repository.list()) == 14
