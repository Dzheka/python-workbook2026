month = int(input())
day = int(input())

if month == 1 and day == 1:
    print("New Year's Day")
elif month == 3 and day == 8:
    print("International Women's Day")
elif month == 3 and 21 <= day <= 24:
    print("Navruz (Persian New Year)")
elif month == 5 and day == 1:
    print("Labour Day")
elif month == 5 and day == 9:
    print("Victory Day")
elif month == 6 and day == 27:
    print("National Unity Day")
elif month == 9 and day == 9:
    print("Independence Day")
elif month == 11 and day == 6:
    print("Constitution Day")
else:
    print("Not a national holiday")
