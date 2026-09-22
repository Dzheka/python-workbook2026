import math

a = float(input("Enter latitude of first point: "))
b = float(input("Enter longitude of first point: "))
c = float(input("Enter latitude of second point: "))
d = float(input("Enter longitude of second point: "))
a = math.radians(a)
b = math.radians(b)
c = math.radians(c)
d = math.radians(d)
e = 6371.01 * math.acos(math.sin(a) * math.sin(c) + math.cos(a) * math.cos(c) * math.cos(b-d))
print(f"Distance: {e:.02f} km")