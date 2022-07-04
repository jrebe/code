"""This module handles schedule information initialized from the schedule_mlb_2019.csv."""
# pylint: disable=unsupported-assignment-operation,E1136

import itertools
import os
import pprint

import pandas as pd


THIS_DIRECTORY = os.path.dirname(__file__)
DATAFILE_PATH = os.path.join(THIS_DIRECTORY, os.pardir, "data", "schedule_mlb_2020.csv")


TEAM_LIST = [
    "Mets",
    "Indians",
    "White Sox",
    "Brewers",
    "Orioles",
    "Blue Jays",
    "Athletics",
    "Padres",
    "Dodgers",
    "Mariners",
    "Reds",
    "Marlins",
    "Rays",
    "Astros",
    "Diamondbacks",
    "Tigers",
    "Cubs",
    "Rangers",
    "Nationals",
    "Yankees",
    "Pirates",
    "Red Sox",
    "Phillies",
    "Royals",
    "Twins",
    "Cardinals",
    "Rockies",
    "Giants",
    "Braves",
    "Angels",
]


class Schedule(object):
    """Class handling functions related to schedule."""

    def __init__(self, datafile=DATAFILE_PATH):
        """Simple init."""
        self._schedule = pd.read_csv(datafile)
        self._games = [Game(scheduled_game) for scheduled_game in self._schedule.to_numpy()]

    @property
    def schedule(self):
        """Schedule property as dataframe."""
        return self._schedule

    @property
    def games(self):
        """List of games property."""
        return self._games

    def team_schedule(self, team):
        """Get a teams schedule."""
        team_schedule = []
        for scheduled_game in self._schedule.to_numpy():
            game = Game(scheduled_game)
            if team == game.home_team:
                team_schedule.append(game)
        return team_schedule

    def park_window(self, team):
        """Generate a park window for the given team."""
        home_games = [game.date for game in self.team_schedule(team)]
        range_list = list(ranges(home_games))
        return range_list


class Game(object):
    """Class that represents a scheduled game."""

    def __init__(self, row):
        """Turn a schedule row into a scheduled game."""
        self._away_team = row[0]
        self._home_team = row[1]
        self._date = row[2]
        self._time = row[3]
        self._datetime = row[4]
        self._uuid = _generate_game_uuid(self.home_team, self.datetime)

    @property
    def home_team(self):
        """The home_team property."""
        return self._home_team

    @property
    def away_team(self):
        """The away_team property."""
        return self._away_team

    @property
    def date(self):
        """The date property."""
        return self._date

    @property
    def time(self):
        """The time property."""
        return self._time

    @property
    def datetime(self):
        """The datetime property."""
        return self._datetime

    @property
    def uuid(self):
        """The uuid property."""
        return self._uuid


def _generate_game_uuid(home_team, datetime):
    """Generate a unique integer id for each game."""
    uuid = int(datetime * 1000) * 100 + TEAM_LIST.index(home_team)
    return uuid


def ranges(iterable):
    """Takes a list of integers and returns contigous ranges as list of tuples."""
    iterable = sorted(set(iterable))
    for _, group in itertools.groupby(enumerate(iterable), lambda t: t[1] - t[0]):
        group = list(group)
        yield group[0][1], group[-1][1]


def ranges_with_gap(range_list, gap=0):
    """Condenses contiguous ranges that span a gap."""
    condensed = []
    current_range = None
    for irange in range_list:
        if current_range is None:
            current_range = irange
        elif current_range[1] + gap + 1 >= irange[0]:
            current_range = (current_range[0], irange[1])
        else:
            condensed.append(current_range)
            current_range = irange
    condensed.append(current_range)
    return condensed


def debug():
    """Debugger used to build module."""
    schedule_data = Schedule()
    print("Park window")
    pprint.pprint(schedule_data.park_window("Red Sox"))


if __name__ == "__main__":
    debug()
