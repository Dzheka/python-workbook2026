#26.5 hours = 1 days, 2 hours, and 30 minutes
#("10.75\n", "10.75 hours = 0 days, 10 hours, and 45 minutes"),
from math import floor

hours = float(input())
days = round(hours // 24)
minutes = round(hours % 1, 2) * 60

print(f"{hours} hours = {days} days, {floor(hours - 24*days)} hours, and {round(minutes)} minutes")