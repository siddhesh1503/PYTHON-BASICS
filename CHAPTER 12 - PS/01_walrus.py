# Using walrus operator
if (n := len([1, 2, 3, 4, 5])) > int(input("Enter a number:")):
    print(f"List is too long with {n} elements")
else:
    print(f"List is of acceptable length with {n} elements")
# Output: List is too long with 5 elements
# Here, the length of the list is assigned to n and then compared to 3 in a single line using the walrus operator (:=).