a = int(input())
if 0<=a<=1:
    print("Infant")
elif 2<=a<=4:
    print("Toddler")
elif 5<=a<=10:
    print("Child")
elif 11<=a<=17:
    print("Adolescent")
elif 18<=a<=39:
    print("Young Adult")
elif 40<=a<=64:
    print("Middle-aged")
elif a>64:
    print("Senior")
else :
    print ("Invalid age")