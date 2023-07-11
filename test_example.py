from elevator import *


def test_accepts_inputs():
    passengers = {
        'Tom': { 'origin': 2, 'destination': 5},
        'Miles': {'origin': 4, 'destination': 10}
    }

    starting_point = 1

    output = elevator_function(passengers, starting_point)

    assert output == 10, "output should be 10"



def test_get_highest_floor():
    passengers = {
        'Tom': { 'origin': 2, 'destination': 5},
        'Miles': {'origin': 4, 'destination': 10}
    }

    starting_point = 1

    output = get_highest_floor(passengers, starting_point)

    assert output == 10


def test_get_highest_floor():
    passengers = {
        'Tom': { 'origin': 2, 'destination': 5},
        'Miles': {'origin': 4, 'destination': 1}
    }

    starting_point = 1

    output = get_highest_floor(passengers, starting_point)

    assert output == 5
