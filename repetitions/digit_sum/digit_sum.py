total = 0
number = abs(int(input()))
while number >0:
    total+= number % 10
    number= number // 10
print(total)
