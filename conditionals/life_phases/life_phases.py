age = int(input())

if age < 0:
    print("Invalid age")
elif age <= 1:
    print("Infant")
elif age <= 4:
    print("Toddler")
elif age <= 10:
    print("Child")
elif age <= 17:
    print("Adolescent")
elif age <= 39:
    print("Young Adult")
elif age <= 64:
    print("Middle-aged")
else:
    print("Senior")