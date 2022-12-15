from aocd import get_data, submit

################################################################################
# Parse input

GRID = get_data(day=12, year=2022).split("\n")
WIDTH = len(GRID[0])
HEIGHT = len(GRID)
# Touch every square once plus one, should be impossible to be a "shortest path"
INFINITY = (WIDTH * HEIGHT) + 1

################################################################################
# Helper Function


def valid_directions(x, y):
    directions = []

    max_value = GRID[y][x] + 1

    if y > 0 and max_value >= GRID[y - 1][x]:
        directions.append((0, -1))
    if y < HEIGHT - 1 and max_value >= GRID[y + 1][x]:
        directions.append((0, 1))
    if x > 0 and max_value >= GRID[y][x - 1]:
        directions.append((-1, 0))
    if x < WIDTH - 1 and max_value >= GRID[y][x + 1]:
        directions.append((1, 0))
    return directions


def dijkstra_multiple_targets(graph, source, targets):
    # Thanks Wikipedia, my memory is not what it used to be:
    # https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm#Pseudocode
    unseen_targets = set(targets)
    dist = {}
    prev = {}
    queue = []
    for v in graph.keys():
        dist[v] = INFINITY
        prev[v] = None
        queue.append(v)
    dist[source] = 0

    while len(queue):
        u = min(queue, key=lambda x: dist[x])

        if u in targets:
            unseen_targets.remove(u)
            if len(unseen_targets) == 0:
                return min([dist[t] for t in targets])

        # delete u from queue
        del queue[queue.index(u)]

        for v in graph[u]:
            if v not in queue:
                continue
            alt = dist[u] + 1
            if alt < dist[v]:
                dist[v] = alt
                prev[v] = u

    return None


################################################################################
# Build data structures

start = None
end = None
for y, row in enumerate(GRID):
    x = row.find("S")
    if x != -1:
        start = (x, y)
        GRID[y] = row.replace("S", "a")

    x = row.find("E")
    if x != -1:
        end = (x, y)
        GRID[y] = row.replace("E", "z")

    if start and end:
        break

for i, row in enumerate(GRID):
    GRID[i] = list(map(ord, row))

GRID[start[1]][start[0]] = ord("a")
GRID[end[1]][end[0]] = ord("z")

# Invert the graph and compute all paths back from the target to all sources
# This lets us solve A and B using the same code
inverted_graph = {}
starting_points = []  # For part B
for y in range(HEIGHT):
    for x in range(WIDTH):
        if GRID[y][x] == ord("a"):
            starting_points.append((x, y))
        # pre-populate all vertices (otherwise, use a defaultdict)
        inverted_graph[(x, y)] = []

for y in range(HEIGHT):
    for x in range(WIDTH):
        for direction in valid_directions(x, y):
            inverted_graph[(x + direction[0], y + direction[1])].append((x, y))


submit(
    dijkstra_multiple_targets(inverted_graph, end, [start]),
    part="a",
    day=12,
    year=2022,
)
submit(
    dijkstra_multiple_targets(inverted_graph, end, starting_points),
    part="b",
    day=12,
    year=2022,
)
