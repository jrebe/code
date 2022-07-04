"""Test main packages."""
# pylint: disable=import-error,no-name-in-module

import unittest

from basebull.optimizer.driving_distance_tsp import create_data_model, print_solution, solve, total_distance


class TestMainMethods(unittest.TestCase):
    """Tests the main functions."""

    def test_create_model(self):
        """Tests creating model."""
        model = create_data_model()
        self.assertIsNotNone(model)

    def test_solve(self):
        """Tests solve method."""
        manager, routing, assignment = solve()
        self.assertIsNotNone(manager)
        self.assertIsNotNone(routing)
        self.assertIsNotNone(assignment)
        self.assertEqual(total_distance(assignment), 17166)

    def test_print(self):
        """Tests solve method."""
        manager, routing, assignment = solve()
        print_solution(manager, routing, assignment)
        self.assertIsNotNone(manager)
        self.assertIsNotNone(routing)
        self.assertIsNotNone(assignment)
        self.assertEqual(total_distance(assignment), 17166)


if __name__ == "__main__":
    unittest.main()
