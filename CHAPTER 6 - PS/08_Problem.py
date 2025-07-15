s = {3, 5, "Sid", 7.5,[1,2] }
# This code will raise an error because lists are mutable and cannot be added to a set
s[4][0] =10
# Output: TypeError: unhashable type: 'list'
