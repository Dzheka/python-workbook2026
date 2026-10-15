n = int(input())

if n %  400 == 0:
    print("Leap year")
elif n % 100 == 0 and n % 400 != 0:
    print("Not leap year")
elif n % 4 == 0 and n % 100 != 0:
    print("Leap year")
else:
    print("Not leap year")