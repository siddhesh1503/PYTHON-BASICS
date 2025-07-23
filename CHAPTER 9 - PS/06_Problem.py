def imch_to_cms(inch):
    return inch * 2.54
n = int(input("Enter value in inches: "))

print(f"The corresponding value in cms is: {imch_to_cms(n)}")