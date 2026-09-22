n=int(input())
if n>=0 and n<=1 :
    print("Infant")
elif n>=2 and n<=4 :
    print("Toddler")
elif n>=5 and n<=10 :
    print("Child")
elif n>=11 and n<=17 :
    print("Adolescent")
elif n>=18 and n<=39 :
    print("Young Adult")
elif n>=40 and n<=64 :
    print("Middle-aged")
elif n>=65 :
    print("Senior")
else :
    print("Invalid age")
