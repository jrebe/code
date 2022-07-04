"""Test util google_maps utils."""
# pylint: disable=import-error,no-name-in-module

import unittest
from unittest.mock import Mock, patch

import lib.map.google_maps as gmaps

DIRECTION_RESULTS = [
    {
        "bounds": {
            "northeast": {"lat": 43.12715360000001, "lng": -71.09696149999999},
            "southwest": {"lat": 37.7790702, "lng": -122.3903569},
        },
        "copyrights": "Map data ©2019 Google, INEGI",
        "legs": [
            {
                "distance": {"text": "3,092 mi", "value": 4975971},
                "duration": {"text": "1 day 22 hours", "value": 164125},
                "duration_in_traffic": {"text": "1 day 21 hours", "value": 162218},
                "end_address": "24 Yawkey Way, Boston, MA 02215, USA",
                "end_location": {"lat": 42.3471753, "lng": -71.09696149999999},
                "start_address": "24 Willie Mays Plaza, San Francisco, CA 94107, " "USA",
                "start_location": {"lat": 37.7790702, "lng": -122.3903569},
                "steps": [
                    {
                        "distance": {"text": "364 ft", "value": 111},
                        "duration": {"text": "1 min", "value": 18},
                        "end_location": {"lat": 37.7797894, "lng": -122.3894796},
                        "html_instructions": "Head <b>northeast</b> on <b>King " "St</b>/<b>Willie Mays Plaza</b>",
                        "polyline": {"points": "evqeFvj_jVi@s@CEOQqAcB"},
                        "start_location": {"lat": 37.7790702, "lng": -122.3903569},
                        "travel_mode": "DRIVING",
                    }
                ],
            }
        ],
    }
]


@patch("lib.map.google_maps.get_maps_client")
class TestUtilGoogleMaps(unittest.TestCase):
    """Tests all maps methods."""

    def test_get_maps_client(self, mocked_client):
        """Test maps client."""
        mocked_client.return_value = Mock()
        mocked_client.return_value.directions.return_value = DIRECTION_RESULTS
        self.assertIsNotNone(gmaps.get_maps_client(api_key="fake"))
        distance = gmaps.driving_distance(str(37.778473), str(-122.389595), str(42.346619), str(-71.096961))
        self.assertEqual(distance, 4975.971)


if __name__ == "__main__":
    unittest.main()
