# Function to get valid numeric input greater than zero
def get_number(prompt):
    while True:
        try:
            num = float(input(prompt))
            if num > 0:
                return num
            print("Number must be greater than zero. Try again.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

while True:
    # Get inputs
    width = get_number("Enter width (greater than zero): ")
    length = get_number("Enter length (greater than zero): ")
    cost_per_meter = get_number("Enter fencing cost per meter (greater than zero): ")

    # Calculate perimeter and fencing cost
    perimeter = 2 * (width + length)
    cost = perimeter * cost_per_meter

    # Display results
    print(f"\nPerimeter: {perimeter:.2f} meters")
    print(f"Fencing Cost: ${cost:.2f}")

    # Ask user if they want another calculation
    if input("\nPress <Enter> to do another calculation, or type anything to quit: "):
        break

