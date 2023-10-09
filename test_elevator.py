from elevator import (
    elevator_function,
    get_highest_floor,
    get_lowest_floor,
    move_elevator,
    brute_force,
    verify_passengers_picked_up,
)

import pytest


def test_elevator_function_signature():
    passengers = {
        "Tom": {"origin": 2, "destination": 5},
        "Miles": {"origin": 4, "destination": 10},
    }

    starting_point = 1

    move_list = elevator_function(passengers, starting_point)

    for x in move_list:
        assert int(x) == x

    for passenger_name, data in passengers.items():
        first_origin_index = move_list.index(data["origin"])
        after_origin_slice = move_list[first_origin_index:]
        assert data["destination"] in after_origin_slice


passengersA = {
    "Tom": {"origin": 2, "destination": 5},
    "Miles": {"origin": 4, "destination": 10},
}

passengersB = {
    "Tom": {"origin": 2, "destination": 5},
    "Miles": {"origin": 4, "destination": 1},
}


@pytest.mark.parametrize(
    ("passengers", "starting_point", "expected_output", "test_function"),
    [
        (passengersA, 1, 10, get_highest_floor),
        (passengersB, 1, 5, get_highest_floor),
        (passengersB, 20, 20, get_highest_floor),
        (passengersA, 1, 1, get_lowest_floor),
        (passengersA, 4, 2, get_lowest_floor),
        (passengersB, 20, 1, get_lowest_floor),
    ],
)
def test_get_highest_or_lowest_floor(
    passengers, starting_point, expected_output, test_function
):
    output = test_function(passengers, starting_point)
    assert output == expected_output


@pytest.mark.parametrize(
    ("start", "destination", "expected"),
    [
        (1, 5, [2, 3, 4, 5]),
        (5, 1, [4, 3, 2, 1]),
    ],
)
def test_move_elevator(start, destination, expected):
    output = move_elevator(start, destination)
    assert output == expected


@pytest.mark.parametrize(
    ("passengers", "starting_point", "expected"),
    [
        (passengersB, 1, [1, 2, 3, 4, 5, 4, 3, 2, 1]),
        (passengersB, 6, [6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1]),
        (passengersA, 1, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]),
    ],
)
def test_brute_force(passengers, starting_point, expected):
    output = brute_force(passengers, starting_point)
    assert output == expected


def test_verify_passengers_picked_up():
    # FIXME: Rewrite now that the output is a list of "moves", rather than a count!

    # Consider breaking this up into multiple sub-functions for easier testability?
    assert True
