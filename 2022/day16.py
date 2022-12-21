from aocd import get_data, submit
import re
from functools import cache

################################################################################
## Common bits

YEAR = 2022
DAY = 16

VALVES = {}
TUNNELS = {}

data = get_data(day=DAY, year=YEAR).split("\n")
for line in data:
    # :sadtrombone:
    # "re module doesn't support repeated captures" - https://stackoverflow.com/a/9765390/11580262
    match = re.match(
        "Valve ([A-Z]+) has flow rate=(\d+); tunnel(:?s)? lead(:?s)? to valve(:?s)? ([A-Z, ]+)",
        line,
    )
    valve, rate, _, _, _, edges = match.groups()
    VALVES[valve] = int(rate)
    TUNNELS[valve] = [e for e in edges.split(", ")]


def print_path(path):
    for p in path:
        print(f"{p[0]} w/ {p[1]} minutes left and closed: {p[2]} ({p[3]})")


################################################################################
## Part A


@cache
def optimal_path(current_location: str, time_remaining: int, off: tuple[str]) -> int:
    off = set(off)
    # Base case, we are either out of time or have turned on everything already
    if time_remaining < 2 or len(off) == 0:
        return 0

    # Is it worth turning on this valve or going someplace else?
    max_pressure_released = 0
    if current_location in off:
        max_pressure_released += VALVES[current_location] * (time_remaining - 1)
        max_pressure_released += optimal_path(
            current_location,
            time_remaining - 1,
            tuple(off - set([current_location])),
        )

    for valve in TUNNELS[current_location]:
        max_pressure_released = max(
            max_pressure_released, optimal_path(valve, time_remaining - 1, tuple(off))
        )

    return max_pressure_released


# No use wasting time checking zero flow valves
starting_state = set(VALVES.keys()) - set(
    [valve for valve, rate in VALVES.items() if rate == 0]
)
# submit(optimal_path("AA", 30, tuple(starting_state)), part="a", day=DAY, year=YEAR)

################################################################################
## Part B
CALL_COUNT = 0


@cache
def optimal_path_with_elephant(
    locations: tuple[str, str],
    time_remaining: int,
    off: tuple[str],
) -> int:
    off = set(off)
    global CALL_COUNT
    CALL_COUNT += 1
    if CALL_COUNT % 100000 == 0:
        print(CALL_COUNT, off)

    # Base case, we are either out of time or have turned on everything already
    if time_remaining < 2 or len(off) == 0:
        return 0

    max_pressure_released = 0
    if locations[0] in off:
        # Case: We both turn our valves
        if locations[1] in off and locations[0] != locations[1]:
            potential_pressure = VALVES[locations[0]] * (time_remaining - 1)
            potential_pressure += VALVES[locations[1]] * (time_remaining - 1)
            new_off = tuple(sorted(list(off - set(locations))))
            potential_pressure += optimal_path_with_elephant(
                locations,
                time_remaining - 1,
                new_off,
            )
            max_pressure_released = max(max_pressure_released, potential_pressure)

        # Case: I turn my valve off, Ellie moves
        for valve in TUNNELS[locations[1]]:
            potential_pressure = VALVES[locations[0]] * (time_remaining - 1)
            new_off = tuple(sorted(list(off - set(locations[:1]))))
            potential_pressure += optimal_path_with_elephant(
                # Improve caching since who is where is not important
                tuple(sorted([locations[0], valve])),
                time_remaining - 1,
                new_off,
            )
            max_pressure_released = max(max_pressure_released, potential_pressure)

    for my_move in TUNNELS[locations[0]]:
        # Case: I move, Ellie turns her valve
        if locations[1] in off:
            potential_pressure = VALVES[locations[1]] * (time_remaining - 1)
            new_off = tuple(sorted(list(off - set(locations[1:]))))
            potential_pressure += optimal_path_with_elephant(
                # Improve caching since who is where is not important
                tuple(sorted([my_move, locations[1]])),
                time_remaining - 1,
                new_off,
            )
            max_pressure_released = max(max_pressure_released, potential_pressure)

        # Case: I move, Ellie moves
        for ellies_move in TUNNELS[locations[1]]:
            new_off = tuple(sorted(list(off)))
            potential_pressure = optimal_path_with_elephant(
                # Improve caching since who is where is not important
                tuple(sorted([my_move, ellies_move])),
                time_remaining - 1,
                new_off,
            )
            max_pressure_released = max(max_pressure_released, potential_pressure)

    return max_pressure_released


tag_team = optimal_path_with_elephant(("AA", "AA"), 26, tuple(starting_state))
print(tag_team)
print(CALL_COUNT)

submit(
    optimal_path_with_elephant(("AA", "AA"), 26, tuple(starting_state)),
    part="b",
    day=DAY,
    year=YEAR,
)
