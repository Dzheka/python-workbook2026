total = 0
count = 0

value = float(input())

while value != 0:
    total += value
    count += 1
    value = float(input())

if count > 0:
    average = total / count
    print(f"The average is {average}")