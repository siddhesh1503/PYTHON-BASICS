words = ["Donkey", "Bad"]

# Read the original file
with open("file.txt", "r") as f:
    content = f.read()

for word in words:
    content = content.replace(word, "#" * len(word))

# Write the new content back
with open("file.txt", "w") as f:
    f.write(content)
