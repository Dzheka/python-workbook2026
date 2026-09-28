year = int(input())

day = (year + (year - 1) // 4 - (year - 1) // 100 + (year - 1) // 400) % 7
if day == 0:
    print("Sunday")
elif day == 1:
    print("Monday")
elif day == 2:
    print("Tuesday")
elif day == 3:
    print("Wednesday")
elif day == 4:
    print("Thursday")
elif day == 5:
    print("Friday")
else:
    print("Saturday")