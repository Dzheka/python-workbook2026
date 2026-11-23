days = int(input("Enter days: "))
hours = int(input("Enter hours: "))
minutes = int(input("Enter minutes: "))
seconds = int(input("Enter seconds: "))

total_seconds = days * 86400 + hours * 3600 + minutes * 60 + seconds

print(total_seconds)