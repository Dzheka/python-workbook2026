a=float(input())
b=float(input())
c=float(input())
sum = a+b+c <=180
if sum and  a<90 and b<90 and c<90 :
    print("Acute Triangle")
elif sum and (a==90 or b==90 or c==90) :
    print("Right Triangle")
elif sum and a>90 or b>90 or c>90 :
    print("Obtuse Triangle")