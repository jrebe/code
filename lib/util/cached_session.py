"""Cached API calls."""
# pylint: disable=too-few-public-methods

import requests

from cachecontrol import CacheControl
from cachecontrol.caches import FileCache

FILE_CACHE_DIRECTORY = ".web_cache"


class CachedSession(object):
    """Simple session cache to reduce repeated API calls."""

    def __init__(self, session=None, cached_session=None):
        """Cached sesssion."""
        if not session:
            session = requests.session()
        self.session = session
        if cached_session:
            self.cached_session = cached_session
        else:
            self.cached_session = CacheControl(session, cache=FileCache(FILE_CACHE_DIRECTORY))

    def get(self, url):
        """HTTP get."""
        return self.cached_session.get(url)
