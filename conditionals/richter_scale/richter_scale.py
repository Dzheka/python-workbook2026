a = float(input())
if a<2:
    print("Micro")
elif 2.0<=a<3.0:
    print("Very Minor")
elif 3.0<=a<4.0:
    print("Minor")
elif 4.0<=a<5.0:
    print("Light")
elif 5.0<=a<6.0:
    print("Moderate")
elif 6.0<=a<7.0:
    print("Strong")
elif 7.0<=a<8.0:
    print("Major")
elif 8.0<=a<10.0:
    print("Great")
elif a>=10:
    print("Meteoric")