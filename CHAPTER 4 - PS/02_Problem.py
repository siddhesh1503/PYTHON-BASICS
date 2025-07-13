letter = '''Dear <|NAME|>,
Greetings from ABC Coding House. We are pleased to inform you that you have been selected for the course. We look forward to your participation.'''

name = input("Enter your name: ")
letter = letter.replace("<|NAME|>", name)
print(letter)