number = abs(int(input()))
count = 0

if number == 0:
    print(1)
    
else:
    while number > 0:
        count += 1
        number //= 10
    print(count)
