l=int(input())
if l%400==0 or (l%4==0 and l%100!=0):
    print("Leap year")
else :
    print("Not leap year")