"""Test main packages."""
# pylint: disable=import-error,no-name-in-module

import unittest
from unittest.mock import patch

from basebull.optimizer.k_means_cluster import kmeans_fit, lat_lon_dataframe, main


class TestMainMethods(unittest.TestCase):
    """Tests the main functions of optimizer."""

    def test_lat_lon_dataframe(self):
        """Tests getting dataframe from park model."""
        coordinates = [(0, 0)]
        dataframe = lat_lon_dataframe(coordinates)
        self.assertIsNotNone(dataframe)

    def test_kmeans_fit(self):
        """Tests fit method."""
        coordinates = [(0, 0)]
        dataframe = lat_lon_dataframe(coordinates)
        kmeans = kmeans_fit(dataframe, 1)
        self.assertIsNotNone(kmeans)

    @patch("matplotlib.pyplot.show")
    def test_main_method(self, mocked_show):
        """Tests fit method."""
        mocked_show.return_value = None
        main()


if __name__ == "__main__":
    unittest.main()
