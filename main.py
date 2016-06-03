import random


def get_random_cell():
    return [
        random.randint(0, 3),
        random.randint(0, 3)
    ]


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
        xy = get_random_cell()
        if is_empty_cell(field, xy):
            return xy

for i in range(5):
    print(get_random_cell())