import math

perimeter = 0.0

first_x = float(input())
first_y = float(input())

prev_x = first_x
prev_y = first_y

while True:
    line = input()
    if line == "":
        break

    curr_x = float(line)
    curr_y = float(input())

    perimeter += math.hypot(curr_x - prev_x, curr_y - prev_y)

    prev_x = curr_x
    prev_y = curr_y

perimeter += math.hypot(first_x - prev_x, first_y - prev_y)

print(f"The perimeter of that polygon is {perimeter}")