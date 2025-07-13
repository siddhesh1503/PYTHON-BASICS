friends = ["Apple", "Banana", "Cherry", "Date"]
print(friends)
# Output: ['Apple', 'Banana', 'Cherry', 'Date']
print(friends[0])  # Output: Apple

friends.append("Elderberry") 
# Correcting the typo in the append method
print(friends)  # Output: ['Apple', 'Banana', 'Cherry', 'Date', 'Elderberry']

friends.insert(1, "Fig")  # Inserting 'Fig' at index 1
print(friends)  # Output: ['Apple', 'Fig', 'Banana', 'Cherry', 'Date', 'Elderberry']

print(friends[1:4])  # Output: ['Fig', 'Banana', 'Cherry']