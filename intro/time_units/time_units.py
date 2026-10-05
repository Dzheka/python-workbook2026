d=int(input("Enter days: "))
h=int(input("Enter hours: "))
m=int(input("Enter minutes: "))
s=int(input("Enter seconds: "))
total=(d*24)*3600
total+=h*3600
total+=m*60
total+=s
print(total)