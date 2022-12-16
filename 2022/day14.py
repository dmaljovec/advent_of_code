from aocd import get_data, submit
from itertools import pairwise

YEAR = 2022
DAY = 14


def attempt_move(x, y):
    if (x, y + 1) not in rocks:
        return (x, y + 1)
    elif (x - 1, y + 1) not in rocks:
        return (x - 1, y + 1)
    elif (x + 1, y + 1) not in rocks:
        return (x + 1, y + 1)
    else:
        return (x, y)


opening = (500, 0)
rock_paths = get_data(day=DAY, year=YEAR).split("\n")

rocks = set()

for path in rock_paths:
    points = [tuple(map(int, point.split(","))) for point in path.split(" -> ")]
    for start, end in pairwise(points):
        if start[0] == end[0]:
            x = start[0]
            for y in range(min(start[1], end[1]), max(start[1], end[1]) + 1):
                rocks.add((x, y))
        elif start[1] == end[1]:
            y = start[1]
            for x in range(min(start[0], end[0]), max(start[0], end[0]) + 1):
                rocks.add((x, y))

original_rocks = set(rocks)

# We are done when a grain of sand is attains a higher value than this height
lowest_rock = max(rocks, key=lambda x: x[1])[1]

while True:
    sand = opening
    next_x, next_y = attempt_move(*sand)
    while next_y != sand[1] and next_y <= lowest_rock:
        sand = (next_x, next_y)
        next_x, next_y = attempt_move(*sand)
    if next_y > lowest_rock:
        break
    rocks.add(sand)

submit(len(rocks) - len(original_rocks), part="a", day=DAY, year=YEAR)

floor = lowest_rock + 2
rocks = set(original_rocks)

while True:
    sand = opening
    next_x, next_y = attempt_move(*sand)
    while next_y != sand[1] and next_y < floor:
        sand = (next_x, next_y)
        next_x, next_y = attempt_move(*sand)
    rocks.add(sand)
    if sand == opening:
        break

submit(len(rocks) - len(original_rocks), part="b", day=DAY, year=YEAR)
