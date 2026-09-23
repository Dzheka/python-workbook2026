hours = float(input())
days = hours / 24
to_hours = hours % 24 
minutes = (to_hours % 1) * 10 * 6

print(f"{hours} hours = {days:.0f} days, {int(to_hours):.0f} hours, and {minutes:.0f} minutes")
