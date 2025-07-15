a = int(input("Enter a age: "))

# if statement no: 1
if(a%2 == 0):
    print(f"{a} is even number")
# End of statement no: 1

# if statement no: 2
if(a > 18):
    print("You are eligible to vote")
elif(a<0):
    print("You entered wrong age")
else:
    print("You are not eligible")
# End of statemet no: 2

