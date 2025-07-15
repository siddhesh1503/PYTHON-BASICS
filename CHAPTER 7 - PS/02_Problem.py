marks1 = int(input("Enter Marks 1: "))
marks2 = int(input("Enter Marks 2: "))
marks3 = int(input("Enter Marks 3: "))

# Check for total percentage
total_percentage = (100*(marks1 + marks2 + marks3))/300

if(total_percentage>=40):
    print("Congrats,You are pass!!")
    print("Your total percentage is: ", total_percentage)

else:
    print("You are failed, Try hard next time!!")
    print("Your total percentage is: ", total_percentage)