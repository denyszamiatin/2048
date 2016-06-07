import random
EMPTY_CELL = 0
DIMENTION = 4

def create_gamefield(dimention, empty_cell):
    '''
    Get number of rows and columns in game field (N rows == N columns)
    and value that marks empty cell. Return game field as a list of lists.
    >>> create_gamefield(4,0)
    [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    >>> create_gamefield(3,1)
    [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
    '''
    row = [int(n) for n in str(empty_cell) * dimention]
    return [row] * dimention


def get_random_cell():
    return [
        random.randint(0, 3),
        random.randint(0, 3)
    ]


def is_empty_cell(field, xy):
    '''
    Get game field as list of lists and 2 coordinates of a cell as list or tuple.
    Return True if cell is empty, otherwise return False.
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
    Get game field as list of lists. Generate new coordinates until corresponding cell is empty.
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