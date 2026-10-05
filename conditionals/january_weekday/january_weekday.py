y=int(input())
d=((y+((y-1)//4))-((y-1)//100)+((y-1)//400))%7
ar=["Sunday", "Monday" ,"Tuesday", "Wednesday", "Thursday", "Friday" ,"Saturday"]
print(ar[d])
