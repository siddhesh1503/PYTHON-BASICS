a = int(input("Enter a number: "))
b = int(input("Enter another number: "))

if b == 0:
    raise ValueError('The second number cannot be zero for divsion.')

else:
    print(f"The division of {a} by {b} is {a / b}")
