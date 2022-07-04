"""Get distance matrix from google maps distance matrix API.

More information is here: https://github.com/googlemaps/google-maps-services-python
"""

import os
import pprint

import googlemaps

THIS_DIR = os.path.dirname(os.path.abspath(__file__))
API_KEY_FILE = os.path.join(THIS_DIR, os.pardir, os.pardir, "maps.key")


def get_api_key(api_key_file=API_KEY_FILE):
    """Just return the maps key for use with static_maps."""
    local_key = None
    with open(api_key_file) as openfile:
        local_key = openfile.readline()
    return local_key


def get_maps_client(api_key=None, api_key_file=API_KEY_FILE):
    """Get the maps client."""
    local_key = None
    if api_key is None:
        with open(api_key_file) as openfile:
            local_key = openfile.readline()
    else:
        local_key = api_key
    return googlemaps.Client(key=local_key)


def driving_distance(lat1, lon1, lat2, lon2, **kwargs):
    """Return simple driving distance."""
    latlon1 = ",".join([lat1, lon1])
    latlon2 = ",".join([lat2, lon2])
    gmap = get_maps_client(**kwargs)
    directions_results = gmap.directions(latlon1, latlon2, mode="driving")
    distance = directions_results[0]["legs"][0]["distance"]["value"]
    distance_km = distance / 1000
    return distance_km


def driving_distance_matrix(coordinate_list, **kwargs):
    """Returns a driving distance matrix between all coordinates."""
    gmap = get_maps_client(**kwargs)
    dm_results_list = []
    for coordinate_pair in coordinate_list:
        dm_results = gmap.distance_matrix(origins=[coordinate_pair], destinations=coordinate_list, mode="driving")
        dm_results_list.append(dm_results)
    return dm_results_list


def debug():
    """Program main."""
    directions = driving_distance_matrix([(37.778473, -122.389595), (42.346619, -71.096961)])
    pprint.pprint(directions)


if __name__ == "__main__":
    print("Getting distance matrix from google.")
    debug()
