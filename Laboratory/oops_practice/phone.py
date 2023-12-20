import csv
from item import Item

class Phone(Item):
    def __init__(self, name: str, price: str, quantity: int, brokenphones=0):
        super().__init__(
            name, price, quantity
        )
        assert brokenphones >= 0, f' broken {brokenphones} is not greater than or equal to zero'

        self.brokenphones = brokenphones


item1 = Item("Phone", 100, 5)
item2 = Item("Laptop", 30, 2)
item2.has_numpad = False
item3 = Item("Mouse", 15, 3)
item4 = Item("USB", 100, 21)
item5 = Item("Cable", 1011, 23)
phone1 = Phone("jscphonev10", 500, 5)
phone1.brokenphones = 1
phone2 = Phone("jscphonev20", 700, 5)
phone2.brokenphones = 2
# print(Item.elements)
# Item.instantiatefromcsv()
# print(Item.isinteger(7.0))
print(Item.elements)
print(Phone.elements)
print(phone1.calculate_total_price())
