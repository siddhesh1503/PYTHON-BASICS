try:
    a = int(input("Enter a number: "))
    print(f"You entered: {a}")

except ValueError as e:
    print(f"Invalid input: {e}")

else:
    print("No exceptions occurred, input was valid.")

# Output will vary based on user input
# The else block runs only if the try block does not raise an exception.
# This demonstrates the use of try, except, and else in exception handling.