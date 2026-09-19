age = int(input())

if 0 <= age <= 1:
    print("Infant")
elif 2 <= age <= 4:
    print("Toddler")
elif 5 <= age <= 10:
    print("Child")
elif 11 <= age <= 17:
    print("Adolescent")
elif 18 <= age <= 39:
    print("Young Adult")
elif 40 <= age <= 64:
    print("Middle-aged")
elif age >= 65:
    print("Senior")
else:
    print("Invalid age")