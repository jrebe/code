"""Calculate distance between coordinates."""
# pylint: disable=invalid-name

from math import atan2, cos, radians, sin, sqrt

R = 6373.0


def distance(lat1, lon1, lat2, lon2):
    """Return simple distance."""
    rlat1 = radians(lat1)
    rlon1 = radians(lon1)
    rlat2 = radians(lat2)
    rlon2 = radians(lon2)
    dlon = rlon2 - rlon1
    dlat = rlat2 - rlat1
    a = sin(dlat / 2) ** 2 + cos(rlat1) * cos(rlat2) * sin(dlon / 2) ** 2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    dist = R * c
    return dist


def distance_matrix(coordinate_list):
    """Returns a distance matrix between all coordinates."""
    dmatrix = []
    for near in coordinate_list:
        distances_away = []
        for far in coordinate_list:
            distances_away.append(distance(near[0], near[1], far[0], far[1]))
        dmatrix.append(distances_away)
    return dmatrix
