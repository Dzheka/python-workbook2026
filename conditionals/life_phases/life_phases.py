a=int(input())
if a==0 or a==1:
    print("Infant")
elif a<=4 and a>=2:
    print("Toddler")
elif a<=10 and a>=5:
    print("Child")
elif a<=17 and a>=11:
    print("Adolescent")
elif a>=18 and a<=39:
    print("Young Adult")
elif a>=40 and a<=64:
    print("Middle-aged")
elif a>=65:
    print("Senior")
else:
    print("Invalid age")