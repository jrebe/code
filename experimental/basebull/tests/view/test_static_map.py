"""Test static maps utils."""

import unittest
from unittest.mock import patch

from basebull.view.static_map import StaticMap, StaticMapsUrl


class TestUtilGoogleMaps(unittest.TestCase):
    """Tests all maps methods."""

    def test_get_maps_client(self):
        """Test maps client."""
        fake_key = "FAKEFAKEFAKEFAKEFAKE"
        self.assertIsNotNone(StaticMapsUrl(center="0, 0", zoom=1, key=fake_key))
        with self.assertRaises(ValueError):
            StaticMapsUrl()
        with self.assertRaises(ValueError):
            StaticMapsUrl(center="0, 0")
        with self.assertRaises(ValueError):
            StaticMapsUrl(center="0, 0", zoom=1, size=None)
        everything_url = StaticMapsUrl(
            center="0, 0", zoom=1, scale=1, map_format="png", maptype="terrain", key=fake_key
        )
        expected_everything = "https://maps.googleapis.com/maps/api/staticmap?center=0%2C+0&zoom=1&size=1024x768&scale=1&format=png&maptype=terrain&key=FAKEFAKEFAKEFAKEFAKE"  # noqa: E501
        self.assertIsNotNone(everything_url)
        self.assertEqual(str(everything_url.url), expected_everything)
        features_url = StaticMapsUrl(markers=["color:blue%7Clabel:S%7C40.702147,-74.015794"], key=fake_key)
        features_string = "https://maps.googleapis.com/maps/api/staticmap?size=1024x768&markers=color%3Ablue%257Clabel%3AS%257C40.702147%2C-74.015794&key=FAKEFAKEFAKEFAKEFAKE"  # noqa: E501
        self.assertIsNotNone(features_url)
        self.assertEqual(str(features_url.url), features_string)

    @patch("basebull.utils.cached_session.CachedSession.get")
    @patch("PIL.ImageFile.Parser")
    def test_get_static_map(self, mock_image, mock_get):
        """Test static map."""
        fake_key = "FAKEFAKEFAKEFAKEFAKE"
        map_url = StaticMapsUrl(center="0, 0", zoom=1, key=fake_key)
        static_map = StaticMap(map_url)
        self.assertIsNotNone(static_map)
        image = static_map.image
        self.assertIsNotNone(image)
        mock_get.return_value.headers = "DEBUG"
        debug = static_map.debug()
        self.assertIsNotNone(debug)
        self.assertEqual(debug, "DEBUG")


if __name__ == "__main__":
    unittest.main()
