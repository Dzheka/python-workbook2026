hour = float(input())
total_minutes=int(hour*60)
day = total_minutes // 1440
hours = (total_minutes % 1440) //60
minute = total_minutes % 60
print(f"{hour} hours = {day} days, {hours} hours, and {minute} minutes")