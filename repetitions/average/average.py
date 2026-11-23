total = 0
count = 0

value = float(input())

while value != 0:
    total += value
    count += 1
    value = float(input())

average = total / count
print(average)
