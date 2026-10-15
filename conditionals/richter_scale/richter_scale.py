a = int(input())

if a < 2:
    print("Micro")
elif a < 3:
    print("Very minor")
elif a < 4:
    print("Minor")
elif a < 5:
    print("Light")
elif a < 6: 
    print("Moderate")
elif a < 7:
    print("Strong")
elif a < 8:
    print("Major")
elif a < 10:
    print("Great")
else:
    print("Meteoric")