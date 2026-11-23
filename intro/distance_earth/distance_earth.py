from math import sin, cos, acos, radians
lat1 = float(input("Enter latitude of first point: "))
lon1 = float(input("Enter longitude of first point: "))
lat2 = float(input("Enter latitude of second point: "))
lon2 = float(input("Enter longitude of second point: "))
lat1 = radians(lat1)
lon1 = radians(lon1)
lat2 = radians(lat2)
lon2 = radians(lon2)
distance = 6371.01 * acos(sin(lat1) * sin(lat2) + cos(lat1) * cos(lat2) * cos(lon1 - lon2))
print(f"Distance: {distance:.2f} km")

