month = input().lower()
day = int(input())

if month == "march" and day >= 20:
    print("Spring")
elif month == "april" or month == "may":
    print("Spring")
elif month == "june" and day <= 20:
    print("Spring")
elif month == "june" and day >= 21:
    print("Summer")
elif month == "july" or month == "august":
    print("Summer")
elif month == "september" and day <= 21:
    print("Summer")
elif month == "september" and day >= 22:
    print("Fall")
elif month == "october" or month == "november":
    print("Fall")
elif month == "december" and day <= 20:
    print("Fall")
else:
    print("Winter")