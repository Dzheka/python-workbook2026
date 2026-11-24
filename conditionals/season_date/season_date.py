"""Logic
Spring: March 20 - June 20
Summer: June 21 - September 21
Fall: September 22 - December 20
Winter: December 21 - March 19"""
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
    "december": 12,
}

month = input().strip().lower()
day = int(input().strip())

date = (months[month], day)

if (3, 20) <= date <= (6, 20):
    print("Spring")
elif (6, 21) <= date <= (9, 21):
    print("Summer")
elif (9, 22) <= date <= (12, 20):
    print("Fall")
else:
    print("Winter")
