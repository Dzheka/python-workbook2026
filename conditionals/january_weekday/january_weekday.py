import math

a = int(input())
b = ((a+((a-1)//4)) - ((a-1)//100) + ((a-1)//400))%7
if b == 0 :
    print("Sunday")
elif b==1:
    print("Monday")
elif b==2:
    print("Tuesday")
elif b==3:
    print("Wednesday")
elif b==4:
    print("Thursday")
elif b==5:
    print("Friday")
elif b==6:
    print("Saturday")
