

def get_input(msgs, opts):
    user_input = None
    while user_input not in opts:
        for msg in msgs:
            print msg
        user_input = raw_input(">> ")
    return user_input


def to_position(x_coord,y_coord):
    try:
        x = int(x_coord)
        y = int(y_coord)
    except ValueError:
        return -1
    else:
        # there should be a better way to do this...
        if x == 1:
            return y - 1
        elif x == 2:
            return y + 2
        else:
            return y + 5

def to_value(player):
    if player == 1:
        return 'X'
    else:
        return 'O'

