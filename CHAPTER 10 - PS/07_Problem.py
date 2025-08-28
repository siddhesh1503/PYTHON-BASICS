
with open("log.text") as f:
    lines = f.readline()
lineno = 1
for line in lines:
    if("python" in line):
        print(f"Yes python is present, Line no: {lineno}")
    lineno += 1
    

else:
    print("No python is not present")