a=int(input())
if a>=0 and a<=1:
    print("Infant")
elif a<=4:
    print("Toddler")
elif a<=10:
    print("Child")
elif a<=17:
    print("Adolescent")
elif a<=39:
    print("Young Adult")
elif a<=64:
    print("Adult")
elif a>=65:
    print("Senior")
else:
    print("Invalid age")