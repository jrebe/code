"""Test parks model."""
# pylint: disable=import-error,no-name-in-module

import unittest

import numpy as np

import basebull.model.ballparks as ballparks


class TestModelBallparksModel(unittest.TestCase):
    """Tests the ballparks model."""

    def test_create_model(self):
        """Test creating model."""
        parks_data = ballparks.Ballparks()
        self.assertIsNotNone(parks_data)

    def test_interact_with_ballparks_model(self):
        """Test interaction with model."""
        parks_data = ballparks.Ballparks()
        self.assertIsNotNone(parks_data.parks_list)
        self.assertIsInstance(parks_data.parks_list, list)
        self.assertEqual(parks_data.park_at_index(0), "Anaheim, CA")
        self.assertEqual(parks_data.get_index_by_city("Anaheim, CA"), 0)
        self.assertIsNotNone(parks_data.direct_distance_matrix())

    def test_distance_matrix(self):
        """Test interaction with model."""
        parks_data = ballparks.Ballparks()
        distance_matrix = parks_data.direct_distance_matrix()
        self.assertIsNotNone(distance_matrix)
        self.assertEqual(round(np.array(parks_data.direct_distance_matrix()).sum()), 1620201)


class TestModelBallparkModel(unittest.TestCase):
    """Tests the ballpark model."""

    def test_create_model(self):
        """Test creating model."""
        fenway = ballparks.Ballpark(
            ["BOS", "Boston Red Sox", "Fenway Park", "Boston, MA", 42.346619, -71.096961, "#BD3039", "ALE"]
        )
        self.assertIsNotNone(fenway)

    def test_interact_with_ballparks_model(self):
        """Test interaction with model."""
        fenway = ballparks.Ballpark(
            ["BOS", "Boston Red Sox", "Fenway Park", "Boston, MA", 42.346619, -71.096961, "#BD3039", "ALE"]
        )
        self.assertEqual(fenway.team, "Boston Red Sox")
        self.assertEqual(fenway.abbreviation, "BOS")
        self.assertEqual(fenway.park, "Fenway Park")
        self.assertEqual(fenway.city, "Boston, MA")
        self.assertEqual(fenway.lat, 42.346619)
        self.assertEqual(fenway.lon, -71.096961)
        self.assertEqual(fenway.color, "#BD3039")
        self.assertEqual(fenway.division, "ALE")
        fenway.distance_array = [0, 10]
        self.assertEqual(fenway.distance_array, [0, 10])


if __name__ == "__main__":
    unittest.main()
