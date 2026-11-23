import math


def distance_earth(lat1, lon1, lat2, lon2):
    lat1 = math.radians(lat1)
    lat2 = math.radians(lat2)
    lon1 = math.radians(lon1)
    lon2 = math.radians(lon2)
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = math.sin(dlat / 2)** 2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2)** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    distance = 6371 * c
    return distance

print(distance_earth(40.7128, -74.0060, 34.0522, -118.2437))
