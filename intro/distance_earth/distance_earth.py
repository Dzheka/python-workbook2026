import math
lat1=float(input("Enter latitude of first point: "))
lon1=float(input("Enter longitude of first point: "))
lat2=float(input("Enter latitude of second point: "))
lon2=float(input("Enter longitude of second point: "))
distance=6371.01*math.acos(math.sin(math.radians(lat1))*math.sin(math.radians(lat2))+math.cos(math.radians(lat1))*math.cos(math.radians(lat2))*math.cos(math.radians(lon1-lon2)))
print(f"Distance: {distance:.2f} km")




