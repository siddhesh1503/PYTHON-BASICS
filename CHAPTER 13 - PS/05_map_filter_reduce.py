l = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, l))
print(squared)

even = list(filter(lambda x: x % 2 == 0, l))
print(even)

from functools import reduce
sum = reduce(lambda x, y: x + y, l)
print(sum)