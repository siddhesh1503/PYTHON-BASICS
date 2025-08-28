class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        return Complex(self.real + other.real, self.imag + other.imag)

    def __mul__(self, other):
        return Complex(self.real * other.real - self.imag * other.imag,
                       self.real * other.imag + self.imag * other.real)

    def __str__(self):
        return f"{self.real} + {self.imag}i"

c1 = Complex(2, 3)
c2 = Complex(4, 5)
c3 = c1 + c2
c4 = c1 * c2
print("Addition:", c3)
print("Multiplication:", c4)
print("Type of c1:", type(c1))
print("Type of c2:", type(c2))
print("Type of c3:", type(c3))
print("Type of c4:", type(c4))