total_hours = float(input())

total_minutes = round(total_hours * 60)
days = total_minutes // 1440
hours = (total_minutes % 1440) // 60
minutes = total_minutes % 60

print(f"{total_hours} hours = {days} days, {hours} hours, and {minutes} minutes")