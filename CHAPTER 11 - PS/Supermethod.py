# super() method is used to access the method of parent class in  child class.

class Car:
    def __init__(self, type):
        self.type = type
        
    @staticmethod
    def start():
        print("Car is started")
    
    @staticmethod
    def stop():
        print("Car is stopped")

class Toyota(Car):
    def __init__(self, name, type):
        self.name = name
        super().__init__(type)


c1 = Toyota("Fortuner", "Disel")
print(c1.type)
print(c1.name)