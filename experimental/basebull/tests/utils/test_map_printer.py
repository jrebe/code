"""Test main maps printer."""
# pylint: disable=import-error,no-name-in-module

import unittest
from unittest.mock import patch

import basebull.utils.map_printer


class TestMainMethods(unittest.TestCase):
    """Tests the main functions."""

    @patch("basebull.utils.map_printer.StaticMap")
    @patch("basebull.utils.map_printer.StaticMapsUrl")
    def test_main_method(self, mock_static_map_url, mock_static_map):
        """Tests creating model."""
        basebull.utils.map_printer.main()


if __name__ == "__main__":
    unittest.main()
