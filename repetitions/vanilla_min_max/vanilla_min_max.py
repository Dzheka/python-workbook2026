value = int(input())

if value != "":
    minimum = value
    maximum = value

    value = int(input())

    while value != "":
        number = value

        if number < minimum:
            minimum = number

        if number > maximum:
            maximum = number

        value = int(input())

print(f"Minimum: {minimum}")
print(f"Maximum: {maximum}")