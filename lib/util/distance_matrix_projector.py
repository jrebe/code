"""Project distance matrix to cartesian plane."""


def distance_matrix_to_map(distance_matrix, labels=None):
    """Returns a map of maps where keys are labels value is distance."""
    if labels is None:
        labels = range(0, len(distance_matrix))
    distance_matrix_map = {}
    for label_source, distance_array in zip(labels, distance_matrix):
        distance_matrix_map[str(label_source)] = {}
        for label_destination, distance in zip(labels, distance_array):
            distance_matrix_map[str(label_source)][str(label_destination)] = distance
    return distance_matrix_map
