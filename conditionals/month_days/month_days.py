n=input().lower()
if n=="january" or n=="march" or n=="may" or n=="july" or n=="august" or n=="october" or n=="december" :
    print("31")
elif n=="april" or n=="june" or n=="september" or n=="november" :
    print("30")
elif n=="february" :
    print("28 or 29")
else :
    print("Invalid month")