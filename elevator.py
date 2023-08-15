import copy


# imperative shell
def elevator_function(passengers, starting_point):
    # FIXME: Better implementation
    return [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]


passengers = {
    "A": {"origin": 1, "destination": 5},
    "B": {"origin": 6, "destination": 4},
}


def brute_force(passengers, starting_point):
    highest_floor = get_highest_floor(passengers, starting_point)
    lowest_floor = get_lowest_floor(passengers, starting_point)

    visited_floors = []
    total_moves = 0

    print("starting on", starting_point)

    print("going to", lowest_floor)

    for floor in range(starting_point, lowest_floor, -1):
        visited_floors.append(floor)

    total_moves += abs(lowest_floor - starting_point)

    print("going to", highest_floor)

    for floor in range(lowest_floor, highest_floor):
        visited_floors.append(floor)

    total_moves += abs(highest_floor - lowest_floor)

    print("back to", lowest_floor)

    for floor in range(highest_floor, lowest_floor, -1):
        visited_floors.append(floor)

    total_moves += abs(lowest_floor - highest_floor)

    return visited_floors


# functional core
def get_highest_floor(passengers, starting_point):
    # passenger_name = Tom, characteristics = {origin / destinations}
    ret_val = starting_point
    for passenger_name, characteristics in passengers.items():
        ret_val = max(ret_val, characteristics["origin"])
        ret_val = max(ret_val, characteristics["destination"])

    return ret_val


# functional core
def get_lowest_floor(passengers, starting_point):
    # passenger_name = Tom, characteristics = {origin / destinations}
    ret_val = starting_point
    for passenger_name, characteristics in passengers.items():
        ret_val = min(ret_val, characteristics["origin"])
        ret_val = min(ret_val, characteristics["destination"])

    return ret_val


# functional core
# assuming that destination should not be the same as origin
def get_is_going_up(origin, destination):
    return destination >= origin


def verify_passengers_picked_up(passengers, current_floor):
    verified_passengers = copy.deepcopy(passengers)
    for passenger_name, passenger_characteristics in verified_passengers.items():
        if passenger_characteristics["origin"] == current_floor:
            passenger_characteristics["origin"] = None
    return verified_passengers
