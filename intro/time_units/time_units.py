"""Enter days: 2
Enter hours: 3
Enter minutes: 45
Enter seconds: 30"""

days = int(input("Days:"))
hours = int(input("Hours:"))
minutes = int(input("Minutes:"))
seconds = int(input("Seconds:"))

total_seconds = seconds + minutes * 60 + hours * 60**2 + days *60**2*24
print(total_seconds)