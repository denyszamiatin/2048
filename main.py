# TODO: def coordinates():
# Here should be a function that generates coordinates -
# issue 4 at GitHub.


def coordinates():
    '''
    For tests
    :return:
    '''
    return [0, 0]

EMPTY_CELL = 0


def is_empty_cell(field, xy):
    '''
    >>> field = [[0, 2], [0, 0]]
    >>> is_empty_cell(field, [0, 0])
    True
    >>> is_empty_cell(field, [0, 1])
    False
    '''
    row = xy[0]
    column = xy[1]
    return field[row][column] == EMPTY_CELL


def get_new_xy(field):
    '''
    >>> field = [[0, 2], [0, 0]]
    >>> get_new_xy(field)
    [0, 0]
    '''
    while True:
        xy = coordinates()
        if is_empty_cell(field, xy):
            return xy
