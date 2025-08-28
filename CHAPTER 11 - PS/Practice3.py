class Circle:
    def __init__(self, radius):
        self.radius = radius

    @staticmethod
    def area(self):
        return 3.14 * self.radius * self.radius
    
    def perimeter(self):
        return 2 * 3.14 * self.radius
    
c1 = Circle(5)
print("Area is:", Circle.area(c1))
print("Perimeter is:", c1.perimeter())
