#Enter days: 2
#Enter hours: 3
#Enter minutes: 45
#Enter seconds: 30
#186330


days=int(input("Enter days: "))
hours=int(input("Enter hours: "))
minutes=int(input("Enter minutes: "))
seconds=int(input("Enter seconds: "))
total_seconds=(days*24*60*60)+(hours*60*60)+(minutes*60)+seconds
print(total_seconds)

