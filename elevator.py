from typing import Dict, List, Tuple

# Example map of Passenger Names -> Data
# (Names could make for easier logging + debugging?)
passengers = {
    "A": {"origin": 2, "destination": 5},
    "B": {"origin": 4, "destination": 10},
}

Passenger = Dict[str, int]

PassengerDict = Dict[str, Passenger]

MoveList = List[int]


# "Imperative shell" showing our intended interface
def elevator_function(passengers: PassengerDict, starting_point: int) -> MoveList:
    # FIXME: this is hardcoded, just to establish what our
    # output should look like - The best path is 1 -> 10
    return [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def worst_case(passengers: PassengerDict, starting_floor: int) -> MoveList:
    """
    Simple, dumb solution that assumes a worst-case scenario
    (Go to the lowest point of interest, then the highest,
    then back down to the lowest again...)

    Our "smart" solutions should be as good, or better!
    """
    highest_floor = get_highest_floor(passengers, starting_floor)
    lowest_floor = get_lowest_floor(passengers, starting_floor)

    visited_floors = [starting_floor]

    print("starting on", starting_floor)

    if lowest_floor != starting_floor:
        this_move = move_elevator(starting_floor, lowest_floor)
        print("going to lowest floor", lowest_floor, this_move)
        visited_floors += this_move

    this_move = move_elevator(lowest_floor, highest_floor)
    print("going up to highest floor", highest_floor, this_move)
    visited_floors += this_move

    this_move = move_elevator(highest_floor, lowest_floor)
    print("returning to", lowest_floor, this_move)
    visited_floors += this_move

    return visited_floors


def second_worst_scenario(passengers: PassengerDict, starting_floor: int) -> MoveList:
    """
    Find the passenger whose Origin is closest to Starting Floor
    Pick them Up
    Go the direction (up/down) that they wanted to go...
        Pick up passengers along that route
        If they match the direction:
    Go to the next Passenger (closest to Starting Floor)
    Repeat
    """
    path = [starting_floor]
    closest_passenger_name = find_closest_passenger(passengers, starting_floor)
    closest_passenger = passengers[closest_passenger_name]
    first_move = move_elevator(starting_floor, closest_passenger["origin"])

    path += first_move
    path += get_delivery_path(closest_passenger, closest_passenger["origin"])

    collected_passengers = list(closest_passenger_name)
    collected, delivered = find_passengers_on_path(passengers, path)
    collected_passengers += collected
    delivered_passengers = []
    delivered_passengers += delivered

    """
    TODO for next time (today is 11/13/2023)
    calculate the additional path for passengers who weren't dropped off
    (for example, if the elevator is going up, and there were passengers going up above
    the initial path, add the trip the the additional floor as well)
    """

    return path


"""
"Functional Core" of simple, purely functional,
"easy to test" units of code (to be used above).

Everything below this point should have Tests, and
ideally be written using Test Driven Development!
"""


def get_highest_floor(passengers, starting_point):
    # Find the highest "interesting" floor in our data set
    ret_val = starting_point
    for passenger_name, characteristics in passengers.items():
        ret_val = max(ret_val, characteristics["origin"])
        ret_val = max(ret_val, characteristics["destination"])

    return ret_val


def get_lowest_floor(passengers, starting_point):
    # Find the lowest "interesting" floor in our data set
    # FIXME: refactor this to be less repetitive?
    ret_val = starting_point
    for passenger_name, characteristics in passengers.items():
        ret_val = min(ret_val, characteristics["origin"])
        ret_val = min(ret_val, characteristics["destination"])

    return ret_val


def get_is_going_up(origin, destination):
    # Is this Passenger going up or down in the building?
    return destination >= origin


def move_elevator(from_floor, to_floor):
    moves = []
    if to_floor > from_floor:
        for x in range(from_floor + 1, to_floor + 1):
            moves.append(x)
    else:
        for x in range(from_floor - 1, to_floor - 1, -1):
            moves.append(x)
    return moves


def find_closest_passenger(passengers: PassengerDict, starting_floor: int) -> str:
    names = list(passengers.keys())
    closest_passenger_name = names[0]
    closest_passenger = passengers[closest_passenger_name]
    lowest_distance = abs(closest_passenger["origin"] - starting_floor)
    for name in names[1:]:
        this_passenger = passengers[name]
        this_distance = abs(this_passenger["origin"] - starting_floor)
        if this_distance < lowest_distance:
            closest_passenger_name = name
            lowest_distance = this_distance

    return closest_passenger_name


def find_passengers_on_path(
    passengers: PassengerDict, path: MoveList
) -> Tuple[List[str], List[str]]:
    origin_passengers = []
    destination_passengers = []
    for name, origin_and_dest in passengers.items():
        if origin_and_dest["origin"] in path:
            origin_passengers.append(name)

        if origin_and_dest["destination"] in path and (name in origin_passengers):
            destination_passengers.append(name)

    return origin_passengers, destination_passengers


def get_delivery_path(passenger: Passenger, starting_floor: int) -> MoveList:
    """
    Automates the process of delivering a single customer, returning a MoveList
    """
    pickup_moves = move_elevator(starting_floor, passenger["origin"])
    delivery_moves = move_elevator(passenger["origin"], passenger["destination"])
    full_moves = pickup_moves + delivery_moves
    print("full_moves", full_moves)
    return full_moves[-1]


def verify_passengers_picked_up(passengers, current_floor, move_list):
    """
    (start of) function to determine if an elevator route
    is "valid", and moves all passengers to destinations...
    """
    if move_list[0] != current_floor:
        return False
    for name, values in passengers.items():
        if not check_passenger_delivered(values, move_list):
            return False
    if not check_moves_are_sequential(move_list):
        return False
    return True


def check_passenger_delivered(passenger, moves):
    try:
        origin_index = moves.index(passenger["origin"])
        moves.index(passenger["destination"], origin_index)
        return True
    except ValueError:
        return False


def check_moves_are_sequential(moves):
    before = moves[0]
    for v in moves[1:]:
        if abs(before - v) != 1:
            return False
        before = v
    return True
