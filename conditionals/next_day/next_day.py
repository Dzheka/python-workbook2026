a = int(input())
b = int(input())
c = int(input())
if b==12:
    if c<31:
        print(f"{a}-{b:02}-{c+1:02}")
    elif c==31:
        print(f"{a+1}-{1:02}-{1:02}")
elif b==1 or b==3 or b==5 or b==7 or a==8 or b==10:
    if c<31:
        print(f"{a}-{b:02}-{c+1:02}")
    elif c==31:
        print(f"{a}-{b+1:02}-{1:02}")
elif b==4 or b==6 or b==9 or b==11:
    if c<30:
        print(f"{a}-{b:02}-{c+1:02}")
    elif c==30:
        print(f"{a}-{b+1:02}-{1:02}")
else :
    if (a%400==0) or (a%4==0 and a%100!=0):
        if c<=28:
            print(f"{a}-{b:02}-{c+1:02}")
        else :
            print(f"{a}-{b+1:02}-{1:02}")
    else:
        if c<=27:
            print(f"{a}-{b:02}-{c+1:02}")
        else :
            print(f"{a}-{b+1:02}-{1:02}")