n=float(input())
if n<2.0 :
    print("Micro")
elif n>=2 and n<3.0:
    print("Very Minor")
elif n>=3 and n<4 :
    print("Minor")
elif n>=4 and n<5 :
    print("Light")
elif n>=5 and n<6 :
    print("Moderate")
elif n>=6 and n<7 :
    print("Strong")
elif n>=7 and n<8 :
    print("Major")
elif n>=8 and n<10 :
    print("Great")
else :
    print("Meteoric")