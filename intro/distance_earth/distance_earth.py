#Enter latitude of first point: 38.5598
#Enter longitude of first point: 68.7870
#Enter latitude of second point: 40.2789
#Enter longitude of second point: 69.6210

#Distance: 204.14 km


#distance = 6371.01 × arccos(sin(lat1) × sin(lat2) + cos(lat1) × cos(lat2) × cos(lon1 - lon2))

#where lat1, lat2, lon1, lon2 are the radian values, and 6371.01 is Earth's average radius in kilometers.

import math

lat1 = float(input("Enter latitude of first point: "))
lon1 = float(input("Enter longitude of first point: "))
lat2 = float(input("Enter latitude of second point: "))
lon2 = float(input("Enter longitude of second point: "))

# Convert degrees to radians
lat1 = math.radians(lat1)
lon1 = math.radians(lon1)
lat2 = math.radians(lat2)
lon2 = math.radians(lon2)

# Calculate the distance
distance = 6371.01 * math.acos(math.sin(lat1) * math.sin(lat2) + math.cos(lat1) * math.cos(lat2) * math.cos(lon1 - lon2))
print(f"Distance: {distance:.2f} km")   

