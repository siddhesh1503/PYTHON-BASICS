class Car:
    def __init__(self):
        self.acc = False
        self.brake = False
        self.clutch = False
    
    def start(self):
        self.acc = True
        self.clutch = True
        self.brake = False
        if self.acc and self.clutch and not self.brake:
            print("Car is started")
        else:
            print("Car is not started")

c1 = Car()
c1.start()
