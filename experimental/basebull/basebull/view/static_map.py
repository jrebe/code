"""Generate static maps using google static maps API."""
# pylint: disable=too-many-arguments,too-many-locals,too-many-branches,bad-continuation
# flake8: ignore=C901

import urllib.parse

from PIL import ImageFile

from basebull.utils.cached_session import CachedSession
from basebull.utils.google_maps import get_api_key


PARAMETER_SEPARATOR = "&"
FEATURE_SEPARATOR = "|"


class StaticMapsUrl(object):
    """Builds a google maps static maps URL (https://developers.google.com/maps/documentation/maps-static/dev-guide)."""

    BASE_URL = "https://maps.googleapis.com/maps/api/staticmap?"
    URL_SIZE_RESTRICTION = 8192
    DEFAULT_MAPS_SIZE = "1024x768"

    def __init__(  # noqa: C901
        self,
        center=None,
        zoom=None,
        size=DEFAULT_MAPS_SIZE,
        scale=None,
        map_format=None,
        maptype=None,
        language=None,
        region=None,
        markers=None,
        path=None,
        visible=None,
        style=None,
        key=None,
        signature=None,
    ):
        """To understand the parameters please refer to Google Static Maps API.

        param names are identical except map_format because python format keyword
        https://developers.google.com/maps/documentation/maps-static/dev-guide
        """
        # Parameters part of URI
        parameter_parts = {}

        # Default map format
        self._map_format = "PNG"

        # Location Parameters
        # Set center and zoom (required if no feature parameters are present)
        if center:
            parameter_parts["center"] = str(center)
        elif not markers and not path:
            raise ValueError("Must provide 'center' if feature parameters not present")

        if zoom:
            parameter_parts["zoom"] = str(zoom)
        elif not markers and not path:
            raise ValueError("Must provide 'zoom' if feature parameters not present")

        # Map Parameters
        # Set size (required)
        if size is None:
            raise ValueError("Must provide valid 'size' parameter")
        parameter_parts["size"] = str(size)
        # Set optional parameters [scale, format, maptype, language, region]
        if scale:
            parameter_parts["scale"] = str(scale)
        if map_format:
            parameter_parts["format"] = str(map_format)
            self._map_format = str(map_format)
        if maptype:
            parameter_parts["maptype"] = str(maptype)
        if language:
            parameter_parts["language"] = str(language)
        if region:
            parameter_parts["region"] = str(region)

        # Feature Parameters
        # Set optional parameters [markers, path, visible, style]
        if markers:
            if isinstance(markers, list):
                parameter_parts["markers"] = FEATURE_SEPARATOR.join(markers)
            else:
                raise ValueError("markers must be a list")
        if path:
            parameter_parts["path"] = FEATURE_SEPARATOR.join(path)
        if visible:
            parameter_parts["visible"] = str(visible)
        if style:
            parameter_parts["style"] = str(style)

        # Key and signature Parameters
        # append api_key
        if key is None:
            key = get_api_key()
            if key is None:
                raise ValueError("Must provide valid 'key' parameter")
        parameter_parts["key"] = str(key)
        if signature:
            parameter_parts["signature"] = str(signature)

        # set parameter parts
        self._parameter_parts = parameter_parts
        self._url = self.BASE_URL + PARAMETER_SEPARATOR.join(parameter_parts)

    @property
    def parameter_parts(self):
        """Returns the parameter_parts."""
        return self._parameter_parts

    @property
    def url(self):
        """Returns the formed url."""
        return self.BASE_URL + urllib.parse.urlencode(self.parameter_parts, doseq=True)

    @property
    def map_format(self):
        """Returns the map format."""
        return self._map_format

    def __str__(self):
        """String format of object."""
        return str(self.url)


class StaticMap(object):
    """StaticMap is an abstraction for handling map downloading, saving, and viewing."""

    def __init__(self, url=None, image_format="PNG"):
        """Initialize the static map."""
        if isinstance(url, StaticMapsUrl):
            self._url = url.url
            self._image_format = url.map_format
        self._url = url
        self._image_format = image_format
        self._image = None

    @property
    def url(self):
        """Returns the formed url."""
        return self._url

    @property
    def image_format(self):
        """Returns the image format."""
        return self._image_format

    @property
    def image(self):
        """Returns the image."""
        if self._image is None:
            self._image = self.download()
        return self._image

    def download(self):
        """Downloads a map and returns an ImageFile."""
        response = CachedSession().get(self.url)
        parser = ImageFile.Parser()
        parser.feed(response.content)
        image = parser.close()
        image.format = self.image_format
        return image

    def debug(self):
        """Downloads a map and returns headers data."""
        response = CachedSession().get(self.url)
        return response.headers

    def view(self, **kwargs):
        """Displays the map image."""
        self.image.show(**kwargs)


def sanitize(param):
    """Returns parameter or dies."""
    if PARAMETER_SEPARATOR in param:
        raise ValueError("Invalid parameter value: %s" % param)
    return param


def debug():
    """Debugger used to build module."""
    maps_url = StaticMapsUrl(key="XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
    print(maps_url.url)


if __name__ == "__main__":
    debug()
