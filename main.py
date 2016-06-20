import random
EMPTY_CELL = 0
DIMENSION = 4
NEW_CELL_IS_2 = 2
NEW_CELL_IS_4 = 4

def create_field():
    '''
    Get number of rows and columns in game field (N rows == N columns)
    and value that marks empty cell. Return game field as a list of lists.
    >>> create_field()
    [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    '''
    return [
        [EMPTY_CELL for _ in range(DIMENSION)]
        for _ in range(DIMENSION)
    ]


def get_random_cell():
    """
    >>> 0 <= get_random_cell()[0] < DIMENSION
    True
    """
    return
        random.randint(0, DIMENSION - 1),
        random.randint(0, DIMENSION - 1)


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
    row, column = xy
    return field[row][column] == EMPTY_CELL


def get_new_xy(field):
    '''
    Get game field as list of lists. Generate new coordinates until corresponding cell is empty.
    '''
    while True:
        xy = get_random_cell()
        if is_empty_cell(field, xy):
            return xy


def get_column(field, y):
    '''
    Get game field and column index. Return column as a list.
    >>> get_column([[2, 4], [0, 2]], 0)
    [2, 0]
    >>> get_column([[2, 4], [0, 2]], 1)
    [4, 2]
    '''
    return [row[y] for row in field]

def get_string(field, x):
    '''
    >>> get_string([1, 2], [3, 4], 0)
    [1, 2]
    >>> get_string([5, 6], [7, 8], 1)
    [7, 8]
    '''
    return [row[x] for row in field]

def shift_values(column, up=True):
    '''
    Get column. Shift non-empty cells to the beginning (if up)
    or end (if down) of the list.
    Return shifted column.
    >>> shift_values([2, 2, 0, 2])
    [2, 2, 2, 0]
    >>> shift_values([0, 2, 0, 4], False)
    [0, 0, 2, 4]
    >>> shift_values([4, 0, 0, 2])
    [4, 2, 0, 0]
    >>> shift_values([2, 4, 2, 0], False)
    [0, 2, 4, 2]
    '''
    empties = column.count(EMPTY_CELL)
    column = remove_empties(column)

    return column + get_empties(empties) if up \
        else get_empties(empties) + column





def get_empties(empties):
    return [EMPTY_CELL for _ in range(empties)]


def remove_empties(column):
    return [cell for cell in column if cell != EMPTY_CELL]

def remove_empties_string(string):
    return [cell for cell in string if cell != EMPTY_CELL]

def merge_values(column, up=True):
    '''
    Get column. Merge non-empty equal values, add empty cells.
    Return merged column.
    >>> merge_values([2, 2, 2, 0])
    [4, 2, 0, 0]
    >>> merge_values([2, 2, 2, 2])
    [4, 4, 0, 0]
    >>> merge_values([2, 2, 2, 2], False)
    [0, 0, 4, 4]
    >>> merge_values([0, 2, 2, 2], False)
    [0, 0, 2, 4]
    >>> merge_values([2, 2, 2, 0])
    [4, 2, 0, 0]
    '''
    if up:
        _merge_column(
            column,
            direction=1,
            start=0,
            end=DIMENSION - 1,
            insert=DIMENSION
        )
    else:
        _merge_column(
            column,
            direction=-1,
            start=DIMENSION - 1,
            end=0,
            insert=0
        )
    return column


def _merge_column(column, direction, start, end, insert):
    for i in range(start, end, direction):
        if column[i] != EMPTY_CELL and column[i] == column[i + direction]:
            column[i] *= 2
            column.pop(i + direction)
            column.insert(insert, EMPTY_CELL)


def return_column(field, column, y):
    '''
    Get game field, column and column index.
    Replace column in game field with a new one.
    >>> return_column([[2, 2, 2, 2], [2, 2, 4, 0], [0, 2, 0, 0], [0, 0, 0, 0]], [4, 2, 0, 0], 1)
    [[2, 4, 2, 2], [2, 2, 4, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    '''
    for x, value in enumerate(column):
        field[x][y] = value
    return field


def merge_values_string(string, left=True):
    '''
    Get column. Merge non-empty equal values, add empty cells.
    Return merged column.
    >>> merge_values_string([2, 2, 2, 0])
    [4, 2, 0, 0]
    >>> merge_values_string([2, 2, 2, 2])
    [4, 4, 0, 0]
    >>> merge_values_string([2, 2, 2, 2], False)
    [0, 0, 4, 4]
    >>> merge_values_string([0, 2, 2, 2], False)
    [0, 0, 2, 4]
    >>> merge_values_string([2, 2, 2, 0])
    [4, 2, 0, 0]
    '''
    if left:
        _merge_string(
            string,
            direction=1,
            start=0,
            end=DIMENSION - 1,
            insert=DIMENSION
        )
    else:
        _merge_string(
            string,
            direction=-1,
            start=DIMENSION - 1,
            end=0,
            insert=0
        )
    return string


def _merge_string(string, direction, start, end, insert):
    for i in range(start, end, direction):
        if string[i] != EMPTY_CELL and string[i] == string[i + direction]:
            string[i] *= 2
            string.pop(i + direction)
            string.insert(insert, EMPTY_CELL)


def return_string(field, string, x):
    '''
    '''
    for y, value in enumerate(string):
        field[x][y] = value
    return field


# zip merge
# for v1, v2 in list(zip(l, l[1:] + [0])):
#  if skip:
#   skip = False
#   continue
#  if v1 == v2:
#   res.append(v1 + v2)
#   skip = True
#  else:
#   res.append(v1)


def generate_number(a=1, b=4):
    number = random.randint(a, b)
    if number < 4:
        return NEW_CELL_IS_2
    else:
        return NEW_CELL_IS_4
