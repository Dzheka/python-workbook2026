import math

lat1 = math.radians(float(input("Enter latitude of first point: ")))
lon1 = math.radians(float(input("Enter longitude of first point: ")))
lat2 = math.radians(float(input("Enter latitude of second point: ")))
lon2 = math.radians(float(input("Enter longitude of second point: ")))

cos_angle = (
    math.sin(lat1) * math.sin(lat2)
    + math.cos(lat1) * math.cos(lat2) * math.cos(lon1 - lon2)
)

distance = 6371.01 * math.acos(max(-1, min(1, cos_angle)))

print(f"Distance: {distance:.2f} km")