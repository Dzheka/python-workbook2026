a = input().lower()
b = int(input())
if a == "march":
    if b>=20:
        print("Spring")
    else :
        print("Winter")
elif a == "april" or a == "may":
    print("Spring")
if a == "june":
    if b>=21:
        print("Summer")
    else :
        print("Spring")
elif a == "july" or a == "august":
    print("Summer")
if a == "september":
    if b>=22:
        print("Fall")
    else :
        print("Summer")
elif a == "october" or a == "november":
    print("Fall")
if a == "december":
    if b>=21:
        print("Winter")
    else :
        print("Fall")
elif a == "january" or a == "february":
    print("Winter")