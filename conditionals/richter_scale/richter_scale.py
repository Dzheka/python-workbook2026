magnitude = float(input())

if magnitude < 2:
    print("Micro")
elif magnitude < 3:
    print("Very Minor")
elif magnitude < 4:
    print("Minor")
elif magnitude < 5:
    print("Light")
elif magnitude < 6:
    print("Moderate")
elif magnitude < 7:
    print("Strong")
elif magnitude < 8:
    print("Major")
elif magnitude < 10:
    print("Great")
else:
    print("Meteoric")