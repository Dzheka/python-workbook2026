month = input().lower()
day = int(input())

months = {
    "january": 1,
    "february": 2,
    "march": 3,
    "april": 4,
    "may": 5,
    "june": 6,
    "july": 7,
    "august": 8,
    "september": 9,
    "october": 10,
    "november": 11,
    "december": 12
}

month_number = months[month]

if (month_number == 3 and day >= 20) or month_number in [4, 5] or (month_number == 6 and day <= 20):
    print("Spring")

elif (month_number == 6 and day >= 21) or month_number in [7, 8] or (month_number == 9 and day <= 21):
    print("Summer")

elif (month_number == 9 and day >= 22) or month_number in [10, 11] or (month_number == 12 and day <= 20):
    print("Fall")

else:
    print("Winter")
    