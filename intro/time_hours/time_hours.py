hours = float(input())

days = int(hours // 24)
remaining_hours = int(hours % 24)
minutes = int((hours % 1) * 60)

print(f"{hours} hours = {days} days, {remaining_hours} hours, and {minutes} minutes")
