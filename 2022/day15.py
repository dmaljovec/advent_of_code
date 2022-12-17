from aocd import get_data, submit
import re
from time import time

################################################################################
## Common bits

YEAR = 2022
DAY = 15

data = get_data(day=DAY, year=YEAR).split("\n")


def manhattan_distance(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)


################################################################################
## Part A

target_row = 2000000

impossible_cols = set()
beacons_in_row = set()
for line in data:
    match = re.match(
        "Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)",
        line,
    )
    sensor_x, sensor_y, beacon_x, beacon_y = map(int, match.groups())
    distance = manhattan_distance(sensor_x, sensor_y, beacon_x, beacon_y)
    remaining_steps = distance - abs(sensor_y - target_row)
    if beacon_y == target_row:
        beacons_in_row.add(beacon_x)
    for x in range(sensor_x - remaining_steps, sensor_x + remaining_steps + 1):
        impossible_cols.add(x)

submit(len(impossible_cols - beacons_in_row), part="a", day=DAY, year=YEAR)

################################################################################
## Part B

MIN = 0
MAX = 4000000

# The single point must lie just outside the boundary of one of our sensors'
# range, otherwise there would be more than one free space
def boundary(x, y, distance):
    distance += 1
    bounds = list()

    for sgn_x in [-1, 1]:
        for sgn_y in [-1, 1]:
            for i in range(distance + 1):
                next_x = x + sgn_x * i
                next_y = y + sgn_y * (distance - i)
                if MIN <= next_x <= MAX and MIN <= next_y <= MAX:
                    bounds.append((next_x, next_y))
    return bounds


sensors = []
for line in data:
    match = re.match(
        "Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)",
        line,
    )
    sensor_x, sensor_y, beacon_x, beacon_y = map(int, match.groups())
    distance = manhattan_distance(sensor_x, sensor_y, beacon_x, beacon_y)
    sensors.append((sensor_x, sensor_y, distance))


# It is a lot faster to shove this all into a giant list and de-dupe it at the
# end (<20 s) compared to continually union-ing sets (~120 s)
start = time()
candidates = list()
for sensor in sensors:
    candidates.extend(boundary(*sensor))
end = time()
print(f"Time to compute all boundaries: {end-start} s")

start = time()
candidates = set(candidates)
end = time()
print(f"Time to dedupe boundaries: {end-start} s")

answer = None
# This is a huge list (~50M), but at least the inner loop here is O(1)
start = time()
for pt in candidates:
    valid = True
    for sensor in sensors:
        if manhattan_distance(pt[0], pt[1], sensor[0], sensor[1]) <= sensor[2]:
            valid = False
            break
    if valid:
        answer = pt[0] * MAX + pt[1]
        break
end = time()
print(f"Time to find a boundary point not within any sensor's field: {end-start}")
submit(answer, part="b", day=DAY, year=YEAR)
