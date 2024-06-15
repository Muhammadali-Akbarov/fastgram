"""
geolocation calculations
"""
import math


def is_within_circle(lat_point, lon_point):
    """
    Check if a given point is within.
    40.1104 and 65.355 is belongs to Navoi
    """
    lat_center_rad = math.radians(40.1104)
    lon_center_rad = math.radians(65.355)
    lat_point_rad = math.radians(lat_point)
    lon_point_rad = math.radians(lon_point)

    dlon = lon_point_rad - lon_center_rad
    dlat = lat_point_rad - lat_center_rad

    a = math.sin(dlat/2)**2 + math.cos(lat_center_rad) * math.cos(lat_point_rad) * math.sin(dlon/2)**2 # noqa
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    distance = 6371 * c

    if distance <= 35:  # Navoi city includes 35km distance
        return True

    return False
