import random
n = random.randint(1, 100)

a = -1
guesses = 0
while a != n:
    a = int(input("Guess a number between 1 and 100: "))

    if a < n:
        print("Too low!")
        guesses += 1
    elif a > n:
        print("Too high!")
        guesses += 1
print(f"You gussed the number {n} correctly in {guesses} attempts!")
# Output will vary as it is random number
