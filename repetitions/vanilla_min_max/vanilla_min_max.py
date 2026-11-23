a = input()

if a != "":
    number = int(a)
    minimum = number
    maximum = number
while True :
    a = input()
    if a=="":
        break
    number = int(a)
    if number < minimum:
            minimum = number

    if number > maximum:
        maximum = number
print(f"Minimum: {minimum}")
print(f"Maximum: {maximum}")