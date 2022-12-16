from aocd import get_data, submit
import re

YEAR = 2022
DAY = 15


def manhattan_distance(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)


data = get_data(day=DAY, year=YEAR).split("\n")
# data = [
#     "Sensor at x=2, y=18: closest beacon is at x=-2, y=15",
#     "Sensor at x=9, y=16: closest beacon is at x=10, y=16",
#     "Sensor at x=13, y=2: closest beacon is at x=15, y=3",
#     "Sensor at x=12, y=14: closest beacon is at x=10, y=16",
#     "Sensor at x=10, y=20: closest beacon is at x=10, y=16",
#     "Sensor at x=14, y=17: closest beacon is at x=10, y=16",
#     "Sensor at x=8, y=7: closest beacon is at x=2, y=10",
#     "Sensor at x=2, y=0: closest beacon is at x=2, y=10",
#     "Sensor at x=0, y=11: closest beacon is at x=2, y=10",
#     "Sensor at x=20, y=14: closest beacon is at x=25, y=17",
#     "Sensor at x=17, y=20: closest beacon is at x=21, y=22",
#     "Sensor at x=16, y=7: closest beacon is at x=15, y=3",
#     "Sensor at x=14, y=3: closest beacon is at x=15, y=3",
#     "Sensor at x=20, y=1: closest beacon is at x=15, y=3",
# ]

target_row = 2000000
# target_row = 10
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
