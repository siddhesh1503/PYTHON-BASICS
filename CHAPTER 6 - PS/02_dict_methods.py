marks = {
    "Siddhesh": 56,
    "Shivam": 57,
    "Vishal": 43,
    "Yogesh": 44,
}
print(marks.items())
print(marks.keys())
print(marks.values())
print(marks.get("Sdiddhesh"))



my_dict = {'name': 'Alice', 'age': 25}

# Access
print(my_dict.get('name'))           # Alice
print(my_dict.get('city', 'Unknown'))# Unknown
print(my_dict.keys())                # dict_keys(['name', 'age'])

# Update
my_dict.update({'city': 'Mumbai'})
print(my_dict)                       # {'name': 'Alice', 'age': 25, 'city': 'Mumbai'}

# Remove
my_dict.pop('age')
print(my_dict)                       # {'name': 'Alice', 'city': 'Mumbai'}
