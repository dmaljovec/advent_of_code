from aocd import get_data, submit
from functools import cache

lines = get_data(day=8, year=2022).split("\n")
GRID = []
for line in lines:
    GRID.append(list(map(int, line)))
WIDTH = len(GRID[0])
HEIGHT = len(GRID)

# The challenge here is not to use numpy for storing the matrix and greatly
# simplifying our ability to slice the data. Perhaps, this will reveal a more
# clever trick to solving the problem.

# Let's keep track of the yet tallest seen tree in my row, so each call to these
# functions is O(1).
@cache
def tallest_left(row, col, stop=0):
    if col == stop:
        return GRID[row][stop]
    return max(tallest_left(row, col - 1, stop), GRID[row][col - 1])


@cache
def tallest_right(row, col, stop=WIDTH - 1):
    if col == stop:
        return GRID[row][stop]
    return max(tallest_right(row, col + 1, stop), GRID[row][col + 1])


@cache
def tallest_above(row, col, stop=0):
    if row == stop:
        return GRID[stop][col]
    return max(tallest_above(row - 1, col, stop), GRID[row - 1][col])


@cache
def tallest_below(row, col, stop=HEIGHT - 1):
    if row == stop:
        return GRID[stop][col]
    return max(tallest_below(row + 1, col, stop), GRID[row + 1][col])


def is_visible(row, col):
    current_tree = GRID[row][col]

    if current_tree > tallest_left(row, col):
        return True

    # Reverse the row and the index and test if any taller to the right
    if current_tree > tallest_right(row, col):
        return True

    # If we use the transposed grid, up is now left
    if current_tree > tallest_above(row, col):
        return True

    # If we use the transposed grid and reverse the row, down is now left
    if current_tree > tallest_below(row, col):
        return True

    return False


# The -2 is to account for the already counted corners
visibile_trees = 2 * WIDTH + 2 * (HEIGHT - 2)
for i in range(1, HEIGHT - 1):
    for j in range(1, WIDTH - 1):
        if is_visible(i, j):
            visibile_trees += 1

submit(visibile_trees, part="a", day=8, year=2022)


@cache
def visible_left(row, col, distance=1):
    if distance == 1:
        value = 1
    elif GRID[row][col] > tallest_right(row, col - distance, col - 1):
        value = 1
    else:
        value = 0

    # Base Case
    if col - distance == 0:
        return value

    return value + visible_left(row, col, distance + 1)


@cache
def visible_right(row, col, distance=1):
    if distance == 1:
        value = 1
    elif GRID[row][col] > tallest_left(row, col + distance, col + 1):
        value = 1
    else:
        value = 0

    # Base Case
    if col + distance == WIDTH - 1:
        return value

    return value + visible_right(row, col, distance + 1)


@cache
def visible_up(row, col, distance=1):
    if distance == 1:
        value = 1
    elif GRID[row][col] > tallest_below(row - distance, col, row - 1):
        value = 1
    else:
        value = 0

    # Base Case
    if row - distance == 0:
        return value

    return value + visible_up(row, col, distance + 1)


@cache
def visible_down(row, col, distance=1):
    if distance == 1:
        value = 1
    elif GRID[row][col] > tallest_above(row + distance, col, row + 1):
        value = 1
    else:
        value = 0

    # Base Case
    if row + distance == HEIGHT - 1:
        return value

    return value + visible_down(row, col, distance + 1)


def scenic_score(row, col):
    return (
        visible_left(row, col)
        * visible_right(row, col)
        * visible_up(row, col)
        * visible_down(row, col)
    )


max_scenic_score = 0
for row in range(1, HEIGHT - 1):
    for col in range(1, WIDTH - 1):
        max_scenic_score = max(max_scenic_score, scenic_score(row, col))

submit(max_scenic_score, part="b", day=8, year=2022)
