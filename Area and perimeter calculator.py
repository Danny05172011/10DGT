# Ask user for width and loop until they 
# enter a number that iws more then zero

hight = 0
width = 0

while True:
    try:
        width = float(input("Enter the width (must be greater than zero): "))
        if width <= 0:
            print("Width must be greater than zero. Try again.")
            continue  # Restart the loop if the input is invalid

        height = float(input("Enter the height (must be greater than zero): "))
        if height <= 0:
            print("Height must be greater than zero. Try again.")
            continue  # Restart the loop if the input is invalid

        # Calculate area and perimeter
        area = round(width * height)
        perimeter =  round(2 * (width + height), 2)

        # Display results
        print(f"Area: {area}")
        print(f"Perimeter: {perimeter}")

        break  # Exit loop
    except ValueError:
        print("PLease enter a number greater than zero")