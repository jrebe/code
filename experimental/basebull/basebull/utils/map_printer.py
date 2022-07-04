"""Prints URL to static maps."""

from __future__ import print_function

import http.client as http_client
import logging

from basebull.model.ballparks import Ballparks
from basebull.view.static_map import StaticMap, StaticMapsUrl


# Set HTTP debugging to log file (https://stackoverflow.com/a/16630836)
http_client.HTTPConnection.debuglevel = 1
logging.basicConfig()
logging.getLogger().setLevel(logging.DEBUG)
LOGGER = logging.getLogger("requests.packages.urllib3")
LOGGER.setLevel(logging.DEBUG)
LOGGER.propagate = True


def main():
    """Is the programs main function."""
    # Get a maps url
    LOGGER.info("Print ballparks URL")
    parks_data = Ballparks()
    all_ballparks_map_url = StaticMapsUrl(markers=parks_data.markers)
    LOGGER.info(all_ballparks_map_url)

    # Get map
    LOGGER.info("Download map")
    all_ballparks_map = StaticMap(all_ballparks_map_url)

    # Get debug information
    LOGGER.info("Get map debug")
    debug_info = all_ballparks_map.debug()
    LOGGER.info(debug_info)

    # View map
    LOGGER.info("View map")
    all_ballparks_map.view()


if __name__ == "__main__":
    main()
