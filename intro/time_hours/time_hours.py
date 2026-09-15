total_hours = float(input())

days = int(total_hours // 24)
remaining_hours = total_hours % 24
hours = int(remaining_hours)
minutes = round((remaining_hours - hours) * 60)

print(f"{total_hours} hours = {days} days, {hours} hours, and {minutes} minutes")