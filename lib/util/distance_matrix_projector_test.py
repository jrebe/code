"""Test util distance_matrix_projector."""
# pylint: disable=import-error,no-name-in-module

import unittest

from lib.util.distance_matrix_projector import distance_matrix_to_map


class TestUtilDmmMethods(unittest.TestCase):
    """Tests all distance matrix projector util methods."""

    def test_distance_matrix_to_map(self):
        """Test conversion of distance matrix."""
        # Matrix
        distance_matrix = [[0, 1.41, 2, 5], [1.41, 0, 1.41, 3.61], [2, 1.41, 0, 2.24], [5, 3.61, 2.24, 0]]
        # Map Expected
        expected = {
            "0": {"0": 0, "1": 1.41, "2": 2, "3": 5},
            "1": {"0": 1.41, "1": 0, "2": 1.41, "3": 3.61},
            "2": {"0": 2, "1": 1.41, "2": 0, "3": 2.24},
            "3": {"0": 5, "1": 3.61, "2": 2.24, "3": 0},
        }
        ddm = distance_matrix_to_map(distance_matrix)
        self.assertEqual(ddm, expected)

        # With labels
        labels = ["a", "b", "c", "d"]
        expected_labels = {
            "a": {"a": 0, "b": 1.41, "c": 2, "d": 5},
            "b": {"a": 1.41, "b": 0, "c": 1.41, "d": 3.61},
            "c": {"a": 2, "b": 1.41, "c": 0, "d": 2.24},
            "d": {"a": 5, "b": 3.61, "c": 2.24, "d": 0},
        }
        ddm_labels = distance_matrix_to_map(distance_matrix, labels)
        self.assertEqual(ddm_labels, expected_labels)
