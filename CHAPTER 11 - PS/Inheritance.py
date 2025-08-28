# Single Inheritance
# When one class (child/derived) derives the properties and methods of another class (parent/base)

class Car:
    @staticmethod
    def start():
        print("Car is started")
    
    @staticmethod
    def stop():
        print("Car is stopped")

class BMW(Car): #inheriting the properties of Car class
    def __init__(self, name, model, year):
        self.name = name
        self.model = model
        self.year = year

b1 = BMW("BMW", "X5", 2025)
print(b1.name, b1.model, b1.year)

# multi-level inheritance
class X7(BMW): #inheriting the properties of BMW class
    def __init__(self, name, model, year, price):
        super().__init__(name, model, year) #calling the constructor of parent class
        self.price = price
    def get_price(self):
        return self.price
x1 = X7("BMW", "X7", 2024, 120000)
print(x1.name, x1.model, x1.year)
print("Price of the car is:", x1.get_price())
Car.start()
Car.stop()