import random
EMPTY_CELL = 0
DIMENSION = 4
NEW_CELL_IS_2 = 2
NEW_CELL_IS_4 = 4
PROBABILITY_OF_4 = .25

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
    return \
        random.randint(0, DIMENSION - 1), \
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


def get_row(field, x):
    '''
    >>> get_string([[1, 2], [3, 4]], 0)
    [1, 2]
    >>> get_string([[5, 6], [7, 8]], 1)
    [7, 8]
    '''
    return field[x]


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


def return_row(field, row, x):
    field[x] = row
    return field


def output(field):
    row_max = [len(str(max(row))) for row in zip(*field)]
    line = ('-') * (sum(row_max) + DIMENSION + 1)

    print(line)
    for row in field:
        print('', end='|')
        for index, cell in enumerate(row):
            print(str(cell).rjust(row_max[index]), end='|')
        print('\n' + line)

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

def generate_number():
    return NEW_CELL_IS_2 \
        if random.random() > PROBABILITY_OF_4 \
        else NEW_CELL_IS_4


def shift_field_vertically(up, field):
    '''
    Get field and direction of shift (up or down).
    Make shift of every column of the field. Return shifted field.
    >>> shift_field_vertically(False, [[2,2,2,4], [2,2,2,4],[0,0,0,0],[2,2,0,0]])
    [[0, 0, 0, 0], [0, 0, 0, 0], [2, 2, 0, 0], [4, 4, 4, 8]]
    >>> shift_field_vertically(True, [[2,2,2,4], [2,2,2,4],[0,0,0,0],[2,2,0,0]])
    [[4, 4, 4, 8], [2, 2, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    '''
    for y in range(DIMENSION):
        column = get_column(field, y)
        new_column = merge_values(shift_values(column, up), up)
        return_column(field, new_column, y)
    return field


def shift_field_horisontally(left, field):
    '''
    Get field and direction of shift (left or right).
    Make shift of every row of the field. Return shifted field.
    >>> shift_field_horisontally(False, [[2,2,2,4], [4,2,2,2],[0,0,0,0],[2,2,0,0]])
    [[0, 2, 4, 4], [0, 4, 2, 4], [0, 0, 0, 0], [0, 0, 0, 4]]
    >>> shift_field_horisontally(True, [[2,2,2,4], [4,2,2,2],[0,0,0,0],[2,2,0,0]])
    [[4, 2, 4, 0], [4, 4, 2, 0], [0, 0, 0, 0], [4, 0, 0, 0]]
    '''
    for x in range(DIMENSION):
        row = get_row(field, x)
        new_row = merge_values(shift_values(row, left), left)
        return_row(field, new_row, x)
    return field


def check_gameover(field):
    '''
    Get field. Return True if there is no empty cells in field, else False.
    >>> check_gameover([[2,2,2,4], [4,2,2,2],[2,2,4,2],[2,2,4,0]])
    False
    >>> check_gameover([[2,2,2,4], [4,2,2,2],[2,2,4,2],[2,2,4,2]])
    True
    '''
    for row in field:
        if EMPTY_CELL in row:
            return False
    return True
