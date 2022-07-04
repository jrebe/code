"""Test util latlong."""
# pylint: disable=import-error,no-name-in-module

import math
import unittest

from basebull.utils.latlong import distance, R


class TestUtilMethods(unittest.TestCase):
    """Tests all util methods."""

    def test_distance(self):
        """Test latlong distance."""
        # somewhere off the coast of west africa
        self.assertEqual(distance(0, 0, 0, 0), 0)
        # ~111 km between points of latitude/longitude at equator
        self.assertEqual(round(distance(1, 0, 0, 0)), 111)
        self.assertEqual(round(distance(0, 1, 0, 0)), 111)
        self.assertEqual(round(distance(0, 0, 1, 0)), 111)
        self.assertEqual(round(distance(0, 0, 0, 1)), 111)
        self.assertEqual(round(distance(-1, 0, 0, 0)), 111)
        self.assertEqual(round(distance(0, -1, 0, 0)), 111)
        self.assertEqual(round(distance(0, 0, -1, 0)), 111)
        self.assertEqual(round(distance(0, 0, 0, -1)), 111)
        # North pole to south pole
        self.assertEqual(round(distance(90, 0, -90, 0)), round(math.pi * R))
        # SF to Boston
        self.assertEqual(round(distance(37.77, 122.41, 42.36, 71.05)), 4335)


if __name__ == "__main__":
    unittest.main()
