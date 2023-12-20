import csv


class Item:
    payrate = 0.8  # payrate after 20% discount
    # magic methods
    elements = []

    def __init__(self, name: str, price: str, quantity=0):
        assert price >= 0, f"{price} is not greater than or equal to zero"
        assert quantity >= 0

        self.name = name
        self.price = price
        self.quantity = quantity

        Item.elements.append(self)
    # methods are functions inside classes

    def calculate_total_price(self):
        self.price = self.price*self.quantity
        return self.price

    def discount(self):
        self.price = self.payrate*self.price
        return self.price

    def __repr__(self):
        return f'{self.__class__.__name__} {self.name}, {self.price}, {self.quantity}'

    @classmethod
    def instantiatefromcsv(cls):
        with open('items.csv') as f:
            reader = csv.DictReader(f)
            items = list(reader)
            for item in items:
                name = item.get("name")
                price = float(item.get("price"))
                quantity = float(item.get("quantity"))

                print(item)

    @staticmethod
    def isinteger(num):
        if isinstance(num, float):
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False
