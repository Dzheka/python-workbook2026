from math import sin, cos, acos, radians

def distance_earth(lat1, lon1, lat2, lon2):
    phi1 = radians(lat1)
    phi2 = radians(lat2)
    lam1 = radians(lon1)
    lam2 = radians(lon2)

    cos_angle = sin(phi1) * sin(phi2) + cos(phi1) * cos(phi2) * cos(lam1 - lam2)

    cos_angle = max(-1.0, min(1.0, cos_angle))

    return 6371 * acos(cos_angle)
