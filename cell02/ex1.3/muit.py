def main():
    try:
        # Prompt for input
        first = int(input("Enter the first number:\n"))
        second = int(input("Enter the second number:\n"))
    except ValueError:
        print("Invalid input. Please enter valid integers.")
        return

    # Calculate the result
    result = first * second

    # Display the multiplication
    print(f"{first} x {second} = {result}")

    # Determine and display the sign
    if result > 0:
        print("The result is positive.")
    elif result < 0:
        print("The result is negative.")
    else:
        print("The result is positive and negative.")

if __name__ == "__main__":
    main()