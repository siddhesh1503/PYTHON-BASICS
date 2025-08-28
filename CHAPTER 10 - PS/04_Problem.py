word = "Donkey"

# Read the original file
with open("file.txt", "r") as f:
    content = f.read()

# Replace the word
contentNew = content.replace(word, "#####")

# Write the new content back
with open("file.txt", "w") as f:
    f.write(contentNew)
