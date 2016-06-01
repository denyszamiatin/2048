# def coordinates():
# Here should be a function that generates coordinates - issue 4 at GitHub.


# Validation of coordinates. A fragment of code that checks for the coordinates (tuple or list)
# whether the corresponding cell of game field (list of lists) is free. If not, it generates a new pair of coordinates.
# The operation repeats until the correct coordinates are generated.

def validation(field, xy):
    row = xy[0]
    column = xy[1]
    if field[row][column] != 0:
        return False
    else:
        return True

def new_coordinates(field):
    check = False
    while check is False:
        xy = coordinates()
        check = validation(field, xy)
    return xy
