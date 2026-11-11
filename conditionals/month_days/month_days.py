a=str(input())
if a=="January" or a=="january" or a=="JANUARY" or a=="May" or a=="may" or a=="MAY" or a=="March" or a=="march" or a=="MARCH" or a=="July" or a=="july" or a=="JULY" or a=="August" or a=="august" or a=="AUGUST" or a=="October" or a=="october" or a=="OCTOBER" or a=="December" or a=="december" or a=="DECEMBER":
    print("31")
elif a=="April" or a=="april" or a=="APRIL" or a=="June" or a=="june" or a=="JUNE" or a=="September" or a=="september" or a=="SEPTEMBER" or a=="November" or a=="november" or a=="NOVEMBER":
    print("30")
elif a=="February" or a=="february" or a=="FEBRUARY":
    print("28 or 29")
else:
    print("Invalid month")
