import math

total = 0

start_x = int(input("Enter the first x-coordinate: "))
start_y = int(input("Enter the first y-coordinate: "))

prev_x, prev_y = start_x, start_y

while True:
    x2 = input("Enter the next x-coordinate (blank to quit): ")

    if x2 == "":
        break

    x2 = int(x2)
    y2 = int(input("Enter the next y-coordinate: "))
    distance = math.dist((prev_x, prev_y), (x2, y2))
    total += distance
    prev_x, prev_y = x2, y2

distance_to_start = math.dist((prev_x, prev_y), (start_x, start_y))
total += distance_to_start

print(f"The perimeter of that polygon is {total}")
