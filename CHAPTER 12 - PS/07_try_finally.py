def main():
    try:
        a = int(input("Enter a number: "))
        print(f"You entered: {a}")

    except ValueError as e:
        print(f"Invalid input: {e}")

    finally:
        print("No exceptions occurred, input was valid.")

main()