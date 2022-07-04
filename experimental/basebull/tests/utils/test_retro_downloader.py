"""Test util retro_downloader."""
# pylint: disable=import-error,no-name-in-module

import unittest
from unittest.mock import patch

from basebull.utils.retro_downloader import main


class TestUtilRetroDownloader(unittest.TestCase):
    """Tests all retro_downloader methods."""

    @patch("urllib.request.urlretrieve")
    def test_create_model(self, mocked_url_retrieve):
        """Test main."""
        mocked_url_retrieve.return_value = None
        main()


if __name__ == "__main__":
    unittest.main()
