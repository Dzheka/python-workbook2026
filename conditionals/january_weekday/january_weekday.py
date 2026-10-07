year = int(input())

day_of_week = (year + (year - 1) // 4 - (year - 1) // 100 + (year - 1) // 400) % 7

if day_of_week == 0:
    print("Sunday")
elif day_of_week == 1:
    print("Monday")
elif day_of_week == 2:
    print("Tuesday")
elif day_of_week == 3:
    print("Wednesday")
elif day_of_week == 4:
    print("Thursday")
elif day_of_week == 5:
    print("Friday")
else:
    print("Saturday")