"""K-means clustering of ballparks."""

from pandas import DataFrame
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

from basebull.model.ballparks import Ballparks


def lat_lon_dataframe(coordinate_list):
    """Return a dataframe with lattitude and longitude of a coordinate list."""
    data = {
        "lat": [lat for lat, lon in coordinate_list],
        "lon": [lon for lat, lon in coordinate_list],
    }
    dataframe = DataFrame(data, columns=["lat", "lon"])
    return dataframe


def kmeans_fit(dataframe, n_clusters):
    """Fit the data into n_clusters and return solution."""
    kmeans = KMeans(n_clusters=n_clusters).fit(dataframe)
    return kmeans


def main():
    """Is the programs main function."""
    # Get ballparks data frame
    ballparks = Ballparks()
    dataframe = lat_lon_dataframe(ballparks.coordinate_list)

    # Walk n_clusters from 1 to max
    for i in range(int(len(ballparks.coordinate_list) / 1.5)):
        kmeans = kmeans_fit(dataframe, i + 1)
        fig = plt.figure()
        fig.canvas.set_window_title("Parks in %s clusters" % str(i + 1))
        plt.scatter(dataframe["lon"], dataframe["lat"], c=kmeans.labels_.astype(float), s=50, alpha=0.5)
        plt.show(block=True)


if __name__ == "__main__":
    main()
