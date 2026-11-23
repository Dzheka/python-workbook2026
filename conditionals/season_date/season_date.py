m=input().lower()
d=int(input())
#ar=["january", "february" , "march", "april" ,"may" ,"june" , "july", "august" ,"september","october","november", "december"]
if m=="march" :
    if d>=20:
        print("Spring")
    else :
        print("Winter")
elif m=="april" or m=="may" :
    print("Spring")
elif m=="june" :
    if d<=20:
        print("Spring")
    else :
        print("Summer")
elif m=="july" or m=="august" :
    print("Summer")
elif m=="september":
    if d<=21:
        print("Summer")
    else :
        print("Fall")
elif m=="october" or m=="november" :
    print("Fall")
elif m=="december" and d<=20:
    print("Fall")
else :
    print("Winter")