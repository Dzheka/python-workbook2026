import math

# Read the first point
first_x = float(input("Enter the first x-coordinate: "))
first_y = float(input("Enter the first y-coordinate: "))

# Initialize perimeter and previous point
perimeter = 0
prev_x = first_x
prev_y = first_y

# Read additional points until blank line
x_input = input("Enter the next x-coordinate (blank to quit): ")
while x_input != "":
    x = float(x_input)
    y = float(input("Enter the next y-coordinate: "))

    # Calculate distance from previous point
    distance = math.sqrt((x - prev_x) ** 2 + (y - prev_y) ** 2)
    perimeter += distance

    # Update previous point
    prev_x = x
    prev_y = y

    # Read next x-coordinate
    x_input = input()

# Add distance from last point back to first point
distance = math.sqrt((first_x - prev_x) ** 2 + (first_y - prev_y) ** 2)
perimeter += distance

# Display result
print(f"The perimeter of that polygon is {perimeter}")
