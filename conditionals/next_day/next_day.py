y=int(input())
m=int(input())
d=int(input())
if m==12:
    if d<=30 :
        print(f"{y}-{m:02}-{d+1:02}")
    else :
        print(f"{y+1}-01-01") 
elif m ==1 or m==3 or m==5 or m==7 or m==8 or m==10 :
    if d<=30 :
        print(f"{y}-{m:02}-{d+1:02}")
    else :
        print(f"{y}-{m+1:02}-01")
elif m ==4 or m==6 or m==9 or m==11 :
    if d<=29 :
        print(f"{y}-{m:02}-{d+1:02}")
    else :
        print(f"{y}-{m+1:02}-01")
else:
    if y % 400 == 0 or (y % 4 == 0 and y % 100 != 0):
        if d <= 28:
            print(f"{y}-{m:02}-{d+1:02}")
        else:
            print(f"{y}-{m+1:02}-01")
    else:
        if d <= 27:
            print(f"{y}-{m:02}-{d+1:02}")
        else:
            print(f"{y}-{m+1:02}-01")