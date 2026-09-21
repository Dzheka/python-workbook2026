a=float(input())
if a<2:
    print("Micro")
elif a>=2 and a<3:
    print("Very Minor")
elif a>=3 and a<4:
    print("Minor")
elif a>=4 and a<5:
    print("Light")
elif a>=5 and a<6:
    print("Moderate")
elif a>=6 and a<7:
    print("Strong")
elif a>=7 and a<8:
    print("Major")
elif a>=8 and a<10:
    print("Great")
else:
    print("Meteoric")
