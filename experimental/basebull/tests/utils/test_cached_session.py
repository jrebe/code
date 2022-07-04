"""Test util cached_session."""
# pylint: disable=import-error,no-name-in-module

import unittest
from unittest.mock import MagicMock, patch

from basebull.utils.cached_session import CachedSession


TEST_URL = "http://localhost/debug"


class TestCachedSession(unittest.TestCase):
    """Tests using a cached session methods."""

    @patch("basebull.utils.cached_session.requests.session")
    def test_session_caching(self, mocked_requests_get):
        """Test main."""
        mocked_requests_get.return_value = MagicMock(get=MagicMock(return_value="Testing"))
        test_session = CachedSession()
        response = test_session.get(TEST_URL)
        self.assertIsNotNone(response)
        self.assertEqual(response, "Testing")
        # Check subsequent call doesn't GET new session mocked return value
        mocked_requests_get.return_value = MagicMock(get=MagicMock(return_value="FAIL"))
        response = test_session.get(TEST_URL)
        self.assertEqual(response, "Testing")


if __name__ == "__main__":
    unittest.main()
