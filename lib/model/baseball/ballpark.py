"""This module handles park information initialized from the parks.csv."""
# pylint: disable=too-many-instance-attributes

import ast
import os
import pprint

import pandas as pd

import lib.util.latlong as latlong
from lib.util.distance_matrix_projector import distance_matrix_to_map
from lib.map.static_map import FEATURE_SEPARATOR


# Fix this
THIS_DIRECTORY = os.path.dirname(__file__)
PARKS_DATAFILE_PATH = os.path.join(THIS_DIRECTORY, os.pardir, "data", "parks.csv")
DISTANCE_DATAFILE_PATH = os.path.join(THIS_DIRECTORY, os.pardir, "data", "distance_matrix_results.txt")


class Ballparks(object):
    """Ballparks is an iterable class containing a list of ball parks."""

    def __init__(self, parks_datafile=PARKS_DATAFILE_PATH, distance_datafile=DISTANCE_DATAFILE_PATH):
        """Simple init."""
        self._raw_parks_list = pd.read_csv(parks_datafile).to_numpy()
        self._parks_list = [Ballpark(row) for row in self._raw_parks_list]
        self._coordinate_list = [park.coordinate_pair for park in self.parks_list]
        with open(distance_datafile) as openfile:
            self._raw_distance_data = ast.literal_eval(openfile.read())
        # Populate distance arrays and distance matrices
        for park, raw_distance_matrix in zip(self._parks_list, self.raw_distance_data):
            distance_array = []
            for row_element in raw_distance_matrix["rows"][0]["elements"]:
                # print(row_element)
                distance_array.append(int(row_element["distance"]["value"] / 1000))
            park.distance_array = distance_array
        self._distance_matrix_map = distance_matrix_to_map(
            [park.distance_array for park in self.parks_list], [park.abbreviation for park in self.parks_list]
        )

    def __iter__(self):
        """Iterator over parks."""
        return self

    def __next__(self):
        """Return next park."""
        for park in self.parks_list:
            yield park

    @property
    def parks_list(self):
        """park_list property."""
        return self._parks_list

    @property
    def coordinate_list(self):
        """coordinate_list property."""
        return self._coordinate_list

    @property
    def raw_distance_data(self):
        """coordinate_list property."""
        return self._raw_distance_data

    @property
    def markers(self):
        """Markers property appropriate for google maps."""
        return [park.marker for park in self.parks_list]

    # Distance matrix functions and helpers

    def direct_distance_matrix(self):
        """Calculates a distance matrix between all parks."""
        return latlong.distance_matrix(self.coordinate_list)

    def driving_distance_matrix(self):
        """Calculates a distance matrix between all parks."""
        return [park.distance_array for park in self.parks_list]

    def park_at_index(self, index):
        """Return park at specific node."""
        return self.parks_list[index].city

    def get_index_by_city(self, city):
        """Return index of city."""
        i = 0
        for park in self.parks_list:
            if park.city == city:
                return i
            i += 1
        return -1


class Ballpark(object):
    """Class to serve as abstraction of individual parks."""

    def __init__(self, row):
        """Init a ballpark."""
        self._abbreviation = row[0]
        self._team = row[1]
        self._park = row[2]
        self._city = row[3]
        self._lat = row[4]
        self._lon = row[5]
        self._color = row[6]
        self._division = row[7]
        self._distance_array = None

    @property
    def abbreviation(self):
        """Team Name."""
        return self._abbreviation

    @property
    def team(self):
        """Team Name."""
        return self._team

    @property
    def park(self):
        """Park Name."""
        return self._park

    @property
    def city(self):
        """Team City."""
        return self._city

    @property
    def lat(self):
        """Park Latitude."""
        return self._lat

    @property
    def lon(self):
        """Park Longitude."""
        return self._lon

    @property
    def coordinate_pair(self):
        """Coordinate pair."""
        return (self.lat, self.lon)

    @property
    def distance_array(self):
        """Coordinate pair."""
        return self._distance_array

    @distance_array.setter
    def distance_array(self, distances):
        self._distance_array = distances

    @property
    def color(self):
        """Marker color of park."""
        return self._color

    @color.setter
    def color(self, color):
        self._color = color

    @property
    def division(self):
        """Division of team."""
        return self._division

    @property
    def marker(self):
        """Google static maps marker."""
        label = ":".join(["label", self.abbreviation])
        lat_long = ",".join([str(self.lat), str(self.lon)])
        marker_format = [label, lat_long]
        if self.color:
            marker_format.append(":".join(["color", self.color]))
        marker_as_string = FEATURE_SEPARATOR.join(marker_format)
        return marker_as_string


def team_color(team):
    """Returns the team color for a given team name."""
    ballparks = Ballparks()
    for park in ballparks.parks_list:
        if park.team == team:
            return park.color
    raise ValueError(f"Team name {team} is not valid")


def debug():
    """Debugger used to build module."""
    parks_data = Ballparks()
    # print("Parks")
    # print(parks_data.parks_list)
    print("distance matrix")
    pprint.pprint(parks_data.driving_distance_matrix())


if __name__ == "__main__":
    debug()
