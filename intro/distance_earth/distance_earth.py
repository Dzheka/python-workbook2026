"""Example 3: Moscow to New York (USA)

Enter latitude of first point: 55.7558
Enter longitude of first point: 37.6176
Enter latitude of second point: 40.7128
Enter longitude of second point: -74.0060

Distance: 7510.29 km
Formula
First convert every coordinate from degrees to radians, then:

distance = 6371.01 × arccos(sin(lat1) × sin(lat2) + cos(lat1) × cos(lat2) × cos(lon1 - lon2))

where lat1, lat2, lon1, lon2 are the radian values, and 6371.01 is Earth's average radius in kilometers."""
from math import sin, cos, acos, radians

lat1 = radians(float(input()))
lon1 = radians(float(input()))

lat2 = radians(float(input()))
lon2 = radians(float(input()))

distance = 6371.01 * acos(sin(lat1) * sin(lat2) + cos(lat1) * cos(lat2) * cos(lon1 - lon2))

print(f"Distance: {distance:.2f} km")