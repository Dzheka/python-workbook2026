first_x = float(input("Enter the first x-coordinate: "))
first_y = float(input("Enter the first y-coordinate: "))
previous_x = first_x
previous_y = first_y
perimeter = 0
while True:
    x = input("Enter the next x-coordinate (blank to quit): ")
    if x == "":
        break
    x = float(x)
    y = float(input("Enter the next y-coordinate: "))
    distance = ((x - previous_x)**2 + (y - previous_y)**2)**0.5
    perimeter += distance
    previous_x = x
    previous_y = y
perimeter += ((first_x - previous_x)**2 + (first_y - previous_y)**2)**0.5
print("The perimeter of that polygon is", perimeter)