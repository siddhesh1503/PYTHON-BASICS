words = {
    "madat": "Help",
    "KHushi": "Happiness",
    "dard": "Pain",
}

word = input("Enter a word: ")
if word in words:
    print(f"The meaning of '{word}' is: {words[word]}")
else:
    print(f"The word '{word}' is not in the dictionary.")
