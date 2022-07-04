"""Test schedule model."""
# pylint: disable=import-error,no-name-in-module

import unittest

from basebull.model.schedule import Game, ranges, ranges_with_gap, Schedule


class TestScheduleModel(unittest.TestCase):
    """Tests the schedule model."""

    def test_create_model(self):
        """Test creating model."""
        schedule_data = Schedule()
        self.assertIsNotNone(schedule_data)
        self.assertIsNotNone(schedule_data.schedule)

    def test_team_schedule(self):
        """Test individual team schedule."""
        schedule_data = Schedule()
        self.assertIsNotNone(schedule_data)
        self.assertEqual(len(schedule_data.schedule), int(162 * 30 / 2))
        team_schedule = schedule_data.team_schedule("Red Sox")
        self.assertEqual(len(team_schedule), 81)

    def test_all_games_unique(self):
        """Test the uniqeness of all games."""
        schedule_data = Schedule()
        games = schedule_data.games
        game_ids = [game.uuid for game in games]
        self.assertEqual(len(game_ids), len(set(game_ids)))

    def test_park_window(self):
        """Test the park windows."""
        schedule_data = Schedule()
        sox_window = schedule_data.park_window("Red Sox")
        self.assertEqual(len(sox_window), 19)


class TestGameModel(unittest.TestCase):
    """Tests the schedule model."""

    def test_create_model(self):
        """Test creating model."""
        go_sox = Game(["Yankees", "Red Sox", 160, 0.799, 160.799])
        self.assertIsNotNone(go_sox)
        self.assertEqual(go_sox.home_team, "Red Sox")
        self.assertEqual(go_sox.away_team, "Yankees")
        self.assertEqual(go_sox.date, 160)
        self.assertEqual(go_sox.time, 0.799)
        self.assertEqual(go_sox.datetime, 160.799)
        self.assertEqual(go_sox.uuid, 16079921)


class TestRangeFunctions(unittest.TestCase):
    """Test the ranges and ranges with gap functions."""

    def test_ranges(self):
        """Test ranges function."""
        ints = [1, 2, 3, 5, 6, 9, 10, 12, 13]
        result = list(ranges(ints))
        self.assertEqual(result, [(1, 3), (5, 6), (9, 10), (12, 13)])

    def test_ranges_with_gap(self):
        """Test ranges function."""
        ints = [1, 2, 3, 5, 6, 9, 10, 12, 13]
        result = list(ranges(ints))
        gap0 = ranges_with_gap(result, 0)
        self.assertEqual(result, gap0)
        gap1 = ranges_with_gap(result, 1)
        expected = [(1, 6), (9, 13)]
        self.assertEqual(expected, gap1)
        gap2 = ranges_with_gap(result, 2)
        expected2 = [(1, 13)]
        self.assertEqual(expected2, gap2)
        gap5 = ranges_with_gap(result, 5)
        expected5 = [(1, 13)]
        self.assertEqual(expected5, gap5)


if __name__ == "__main__":
    unittest.main()
