first_input = input()
first_value = int(first_input)
min_value = first_value
max_value = first_value

while True:
    line = input()
    if line == "":
        break
    value = int(line)
    if value < min_value:
        min_value = value
    if value > max_value:
        max_value = value

print(f"Minimum: {min_value}")
print(f"Maximum: {max_value}")
