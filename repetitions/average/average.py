total = 0
count = 0
number = int(input())
while number != 0:
    total = total + number
    count = count + 1
    number = float(input())
    if count > 0:
        print("The average is", total / count)
