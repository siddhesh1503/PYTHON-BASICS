class Order:
    def __init__(self, item, price):
        self.item = item
        self.price = price


    def __gt__(self, other):
        return self.price > other.price

o1 = Order("Laptop", 50000)
o2 = Order("Mobile", 20000)
if o1 > o2:
    print(f"{o1.item} is costlier than {o2.item}")
else:
    print(f"{o2.item} is costlier than {o1.item}")
# > operator is overloaded here using static method
