# Riho Luik
# Küsimused ning vastused!

# K - Kuidas sa testisid?
# V - Ma testisin seda kontrollides koodis antud funktsioone tegimist csv'ga.
#     Ma leidsin, et algses koodis puudus print funktsioon, discount funktsiooni lisamine
#     ning sisaldas üht ebavajaliku funktsiooni, mis ei andnud koodile midagi juurde.

# K - Milliseid järeldusi koodi funktsioneerimise kohta sain teada?
# V - Koodis võib olla ebavajaliku funktsiooni, mis võimalusel ei anna koodile midagi juurde.
#     Võib puududa ka funktsioon või kaks, mis peatab koodi mõeldud funktsioneerimist
#     ehk siin seisus puudus funktsioon, et lisada discount, liita kokku asjade hinnad
#     ning neid ka väljastada.


import csv

class Item:
    pay_rate = 0.8  # The pay rate after 20% discount
    all = []

    def __init__(self, name: str, price: float, quantity=0):
        assert price >= 0, f"Price {price} is not greater than or equal to zero!"
        assert quantity >= 0, f"Quantity {quantity} is not greater or equal to zero!"

        self.name = name
        self.price = price
        self.quantity = quantity

        Item.all.append(self)

    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * self.pay_rate

    @classmethod
    def instantiate_from_csv(cls):
        with open('items.csv', 'r') as f:
            reader = csv.DictReader(f, delimiter=';')
            items = list(reader)

        for item in items:
            print(f"{item}")  # Debugging output

            Item(
                name=item.get('name'),
                price=float(item.get('price')),
                quantity=int(item.get('quantity')),
            )

    def __repr__(self):
        return f"Item('{self.name}', {self.price}, {self.quantity})"

# Call it **AFTER** the class definition
Item.instantiate_from_csv()

print("\nAll items created:", Item.all)

for item in Item.all:
    print(f"\nItem: {item.name}")
    print(f"Price per Item: {item.price}")
    print(f"Total Price: {item.calculate_total_price()}")
    item.apply_discount()
    print(f"Discounted Price per Items: {item.price}")
    print(f"Discounted Price for All Items: {item.calculate_total_price()}")