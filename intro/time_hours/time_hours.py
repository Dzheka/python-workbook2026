a = float(input())
b = a // 24
c = ((a - (b * 24))*60)//60
d = ((a - (b * 24))*60)%60
print(f"{a} hours = {b:.0f} days, {c:.0f} hours, and {d:.0f} minutes")