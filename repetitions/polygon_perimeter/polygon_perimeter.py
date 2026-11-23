import math

first_x = float(input("Enter the first x-coordinate: "))
first_y = float(input("Enter the first y-coordinate: "))

perimeter = 0
prev_x = first_x
prev_y = first_y

x_input = input("Enter the next x-coordinate (blank to quit): ")
while x_input != "":
    x = float(x_input)
    y = float(input("Enter the next y-coordinate: "))

    distance = math.sqrt((x - prev_x) ** 2 + (y - prev_y) ** 2)
    perimeter += distance

    prev_x = x
    prev_y = y

    x_input = input()

# Close the polygon: last point back to the first
distance = math.sqrt((first_x - prev_x) ** 2 + (first_y - prev_y) ** 2)
perimeter += distance

print(f"The perimeter of that polygon is {perimeter}")
