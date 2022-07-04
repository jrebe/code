"""Download historic MLB schedules."""

import urllib.request

URL_BASE = "http://www.retrosheet.org/schedule/"
ZIPS_FOLDER = "../data/zips/"
YEARS = range(1877, 2020)


def main():
    """Program main."""
    for year in YEARS:
        url = "".join([URL_BASE, str(year), "SKED.ZIP"])
        urllib.request.urlretrieve(url, "".join([ZIPS_FOLDER, "mlb_schedule_", str(year), ".zip"]))
        print("Downloaded %s" % year)


if __name__ == "__main__":
    print("downloading schedules from retrosheet")
    main()
