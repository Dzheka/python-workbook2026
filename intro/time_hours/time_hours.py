#26.5

#26.5 hours = 1 days, 2 hours, and 30 minutes
hours = float(input("Enter the number of hours: "))
days = int(hours // 24)
remaining_hours = hours % 24
minutes = int((remaining_hours % 1) * 60)
print(f"{hours} hours = {days} days, {int(remaining_hours)} hours, and {minutes} minutes")
