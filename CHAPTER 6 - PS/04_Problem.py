s = set()
s.add(20)
s.add(20.0)
s.add("20")
print(s)
# yes we can add different data types to a set
# Output: {20, 20.0, '20'}
# yes, sets can contain different data types, but they will be treated as distinct elements if they are not equal