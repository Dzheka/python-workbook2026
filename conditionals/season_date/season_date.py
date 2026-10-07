month = input().lower()
day = int(input())

if (month == "march" and day >= 20) or month == "april" or month == "may" or (month == "june" and day <= 20):
    print("Spring")
elif (month == "june" and day >= 21) or month == "july" or month == "august" or (month == "september" and day <= 21):
    print("Summer")
elif (month == "september" and day >= 22) or month == "october" or month == "november" or (month == "december" and day <= 20):
    print("Fall")
else:
    print("Winter")