m=int(input())
d=int(input())
if m==1 and d==1 :
    print("New Year's Day")
elif m==3 and d==8:
    print("International Women's Day")
elif m==3 and (d==21 or d==22 or d==23 or d==24):
    print("Navruz (Persian New Year)")
elif m==5 and d==1 :
    print("Labour Day")
elif m==5 and d==9 :
    print("Victory Day")
elif m==6 and d==27 :
    print("National Unity Day")
elif m==9 and d==9:
    print("Independence Day")
elif m==11 and d==6 :
    print("Constitution Day")
else :
    print("Not a national holiday")
