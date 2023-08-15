import copy

# Example map of Passenger Names -> Data
# (Names could make for easier logging + debugging)
passengers = {
    "A": {"origin": 2, "destination": 5},
    "B": {"origin": 4, "destination": 10},
}


# "Imperative shell" showing our intended interface
def elevator_function(passengers, starting_point):
    # FIXME: this is hardcoded, just to establish what our
    # output should look like - The best path is 1 -> 10
    return [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def brute_force(passengers, starting_floor):
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

    if (lowest_floor != starting_floor):
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


def verify_passengers_picked_up(passengers, current_floor, move_list):
    """
    (start of) function to determine if an elevator route
    is "valid", and moves all passengers to destinations...
    """
    # FIXME: Rewrite now that we return a list of moves, instead of a count!

    # assert that all moves are sequential integers
    #       (exactly within 1 index of each other?)

    # assert that all passenger origins appear in the move list

    # assert that all passenger destinations appear in the move list

    # assert that a given Passenger's Origin appears before their Destination

    #      (It is okay for either to appear multiple times)


def move_elevator(from_floor, to_floor):
    moves = []
    if to_floor > from_floor:
        for x in range(from_floor+1, to_floor + 1):
            moves.append(x)
    else:
        for x in range(from_floor-1, to_floor - 1, -1):
            moves.append(x)
    return moves
