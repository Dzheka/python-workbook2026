a = input().capitalize()
b = int(input())
if (a == "March" and b >= 20) or a in ("April", "May") or (a == "June" and b < 21):
    print("Spring")
elif (a == "June" and b >= 21) or a in ("July", "August") or (a == "September" and b < 22):
    print("Summer")
elif (a == "September" and b >= 22) or a in ("October", "November") or (a == "December" and b < 21):
    print("Fall")
else:
    print("Winter")