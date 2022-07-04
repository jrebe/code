"""Solves simple travelling salesman problem between ballparks with schedule constraints."""
# pylint: disable=no-member,duplicate-code

from __future__ import print_function

from ortools.constraint_solver import pywrapcp, routing_enums_pb2

from basebull.model.ballparks import Ballparks
from basebull.model.schedule import Schedule


def create_data_model():
    """Creates data model for the problem."""
    data = {}
    parks_data = Ballparks()
    schedule_data = Schedule()
    data["distance_matrix"] = parks_data.driving_distance_matrix()
    data["home"] = parks_data.get_index_by_city("San Francisco, CA")
    # [(0,5), (10,13)] schedule format
    data["schedule_matrix"] = [schedule_data.park_window(park.team) for park in parks_data.parks_list]
    # [0, 1, 2, 3, 4, 5, 10, 11, 12, 13] schedule format
    # data["game_matrix"] = [schedule_data.team_schedule(park.team) for park in parks_data.parks_list]
    data["num_people"] = 1
    return data


def main():
    """Is the programs main function."""
    # Solve the problem.
    # manager, routing, assignment = solve()
    # Print solution on console.
    # if assignment:
    #    print_solution(manager, routing, assignment)
    data = create_data_model()
    import pprint

    pprint.pprint(data)


if __name__ == "__main__":
    main()
