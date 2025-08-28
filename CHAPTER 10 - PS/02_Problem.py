import random

def game():
    print("You are playing the game.")
    score = random.randint(1, 62)

    # Fetch the hiscore
    try:
        with open("hiscore.txt") as f:
            hiscore = f.read()
            if hiscore != "":
                hiscore = int(hiscore)
            else:
                hiscore = 0
    except FileNotFoundError:
        hiscore = 0  # If file doesn't exist yet

    print(f"Your score: {score}")
    
    if score > hiscore:
        print("Congratulations! New high score!")
        with open("hiscore.txt", "w") as f:
            f.write(str(score))  # Convert to string before writing
    else:
        print(f"High score remains: {hiscore}")
    
    return score

game()
