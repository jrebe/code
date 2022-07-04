"""Solves simple travelling salesman problem between ballparks."""
# pylint: disable=no-member,duplicate-code

from __future__ import print_function

from ortools.constraint_solver import pywrapcp, routing_enums_pb2

from basebull.model.ballparks import Ballparks


def create_data_model():
    """Creates data model for the problem."""
    data = {}
    parks_data = Ballparks()
    data["distance_matrix"] = parks_data.driving_distance_matrix()
    data["home"] = parks_data.get_index_by_city("San Francisco, CA")
    data["num_people"] = 1
    return data


def print_solution(manager, routing, assignment):
    """Prints assignment on console."""
    print("Total distance: {} kms".format(total_distance(assignment)))
    index = routing.Start(0)
    plan_output = "Route:\n"
    route_distance = 0
    parks_data = Ballparks()
    while not routing.IsEnd(index):
        plan_output += " {} ->".format(parks_data.park_at_index(manager.IndexToNode(index)))
        previous_index = index
        index = assignment.Value(routing.NextVar(index))
        route_distance += routing.GetArcCostForVehicle(previous_index, index, 0)
    plan_output += " {}\n".format(parks_data.park_at_index(manager.IndexToNode(index)))
    print(plan_output)
    plan_output += "Route distance: {}miles\n".format(route_distance)


def solve():
    """Solves the optimization problem."""
    # Instantiate the data problem.
    data = create_data_model()

    # Create the routing index manager.
    manager = pywrapcp.RoutingIndexManager(len(data["distance_matrix"]), data["num_people"], data["home"])

    # Create Routing Model.
    routing = pywrapcp.RoutingModel(manager)

    def distance_callback(from_index, to_index):
        """Returns the distance between the two nodes."""
        # Convert from routing variable Index to distance matrix NodeIndex.
        from_node = manager.IndexToNode(from_index)
        to_node = manager.IndexToNode(to_index)
        return data["distance_matrix"][from_node][to_node]

    transit_callback_index = routing.RegisterTransitCallback(distance_callback)

    # Define cost of each arc.
    routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)

    # Setting first solution heuristic.
    search_parameters = pywrapcp.DefaultRoutingSearchParameters()
    search_parameters.first_solution_strategy = routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC

    # Solve the problem.
    assignment = routing.SolveWithParameters(search_parameters)

    return manager, routing, assignment


def total_distance(assignment):
    """Returns total distance of assignment."""
    return assignment.ObjectiveValue()


def main():
    """Is the programs main function."""
    # Solve the problem.
    manager, routing, assignment = solve()
    # Print solution on console.
    if assignment:
        print_solution(manager, routing, assignment)


if __name__ == "__main__":
    main()
