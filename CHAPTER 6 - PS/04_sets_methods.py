a = {1, 2, 3}
b = {3, 4, 5}

# Add and Remove
a.add(6)             # {1, 2, 3, 6}
a.discard(2)         # {1, 3, 6}
a.remove(3)          # {1, 6}

# Set Operations
print(a.union(b))    # {1, 4, 5, 6, 3}
print(a & b)         # {3}
print(a - b)         # {1, 6}
print(a ^ b)         # {1, 4, 5, 6}

# Subset
print(a.issubset(b)) # False
