import os

def generatetable(n):
    # Make sure 'tables' folder exists
    os.makedirs("tables", exist_ok=True)

    table = ""
    for i in range(1, 11):
        table += f"{n} X {i} = {n*i}\n"
    
    with open(f"tables/table_{n}.txt", "w") as f:  # Added .txt extension
        f.write(table)

for i in range(1, 21):
    generatetable(i)
