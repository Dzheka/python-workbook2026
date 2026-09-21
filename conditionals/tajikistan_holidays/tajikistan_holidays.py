a = int(input())
b = int(input())
if a == 1 and b == 1 :
    print("New Year's Day ") 
elif a == 3 and 21<=b<=24 :
    print ("Navruz (Persian New Year)")
elif a == 3 and b == 8:
    print("International Women's Day")
elif a == 5 and b == 1:
    print("Labour Day")
elif a == 5 and b == 9:
    print("Victory Day")
elif a == 6 and b == 27 :
    print("National Unity Day")
elif a == 9 and b == 9:
    print("Independence Day")
elif a == 11 and b == 6:
    print("Constitution Day")
else :
    print("Not a national holiday")