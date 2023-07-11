# imperative shell
def elevator_function(passengers, starting_point):
    print(1)
    return 10


# functional core
def get_highest_floor(passengers, starting_point):
    # passenger_name = Tom, characteristics = {origin / destinations}
    ret_val = starting_point
    for passenger_name, characteristics in passengers.items():
        ret_val = max(ret_val, characteristics['origin'])
        ret_val = max(ret_val, characteristics['destination'])

    return ret_val


# functional core
def get_lowest_floor():
    pass

# functional core
# assuming that destination should not be the same as origin
def get_is_going_up(origin, destination):

    return destination >= origin
