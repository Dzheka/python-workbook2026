from math import radians,cos,sin,acos


lat1 = radians(float(input("Enter latitude of first point: ")))
lon1 = radians(float(input("Enter longitude of first point: ")))
lat2 = radians(float(input("Enter latitude of second point: ")))
lon2 = radians(float(input("Enter longitude of second point: ")))

distance = 6371.01 * acos(sin(lat1) * sin(lat2) + cos(lat1) * cos(lat2) * cos(lon1 - lon2))
print(f"Distance: {distance:.2f} km")