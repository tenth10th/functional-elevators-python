from elevator import (
    elevator_function,
    get_highest_floor,
    get_lowest_floor,
    brute_force,
    verify_passengers_picked_up,
)

from pytest import mark


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


@mark.parametrize(
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


def test_brute_force():
    starting_point = 2
    output = brute_force(passengersB, starting_point)
    # from 2 go down to 1 up to 5 then back down to 1
    assert output == 1 + 4 + 4


def test_verify_passengers_picked_up():
    current_floor = 2
    verified_passengers_a = verify_passengers_picked_up(passengersA, current_floor)
    assert verified_passengers_a["Tom"]["origin"] is None
