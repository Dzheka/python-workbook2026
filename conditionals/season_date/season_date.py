month = input().lower()
day = int(input())

if month == "march":
    if day >= 20:
        print("Spring")
    else:
        print("Winter")
elif month == "april" or month == "may":
    print("Spring")
elif month == "june":
    if day >= 21:
        print("Summer")
    else:
        print("Spring")
elif month == "july" or month == "august":
    print("Summer")
elif month == "september":
    if day >= 22:
        print("Fall")
    else:
        print("Summer")
elif month == "october" or month == "november":
    print("Fall")
elif month == "december":
    if day >= 21:
        print("Winter")
    else:
        print("Fall")
else:
    print("Winter")
