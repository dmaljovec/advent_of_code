from aocd import get_data, submit

################################################################################
## Common bits

YEAR = 2022
DAY = 18

locations = [
    tuple(map(int, line.split(",")))
    for line in get_data(day=DAY, year=YEAR).split("\n")
]

################################################################################
## Part A


def adjacent(x1, y1, z1, x2, y2, z2):
    return abs(x1 - x2) + abs(y1 - y2) + abs(z1 - z2) == 1


def get_exposed_face_count(locations):
    uncovered_faces = {}
    for lava in locations:
        uncovered_faces[lava] = 6
        for seen in uncovered_faces.keys():
            if adjacent(*seen, *lava):
                uncovered_faces[lava] -= 1
                uncovered_faces[seen] -= 1
    return sum(uncovered_faces.values())


submit(get_exposed_face_count(locations), part="a", day=DAY, year=YEAR)

################################################################################
## Part B

# Create a bounding box, invert the set, and use a Union-Find data structure to
# compute connected components of the inner stuff. We can then compute the
# surface area of those holes and subtract it from part A


class Singleton(object):
    def __init__(self, id):
        self.id = id
        self.parent = id
        self.rank = 0


class UnionFind(object):
    def __init__(self):
        self.sets = {}

    def make_set(self, id):
        if id not in self.sets:
            self.sets[id] = Singleton(id)
        return self.sets[id]

    def find(self, id):
        if id not in self.sets:
            self.make_set(id)

        if self.sets[id].parent == id:
            return id
        else:
            self.sets[id].parent = self.find(self.sets[id].parent)
            return self.sets[id].parent

    def union(self, x, y):
        xRoot = self.find(x)
        yRoot = self.find(y)

        if xRoot == yRoot:
            return

        if (self.sets[xRoot].rank < self.sets[yRoot].rank) or (
            self.sets[xRoot].rank < self.sets[yRoot].rank and xRoot < yRoot
        ):
            self.sets[xRoot].parent = yRoot
            self.sets[yRoot].rank = self.sets[yRoot].rank + 1
        else:
            self.sets[yRoot].parent = xRoot
            self.sets[xRoot].rank = self.sets[xRoot].rank + 1

    def count_components(self):
        return len(self.get_component_representatives())

    def get_component_representatives(self):
        roots = set()
        for key in self.sets:
            root = self.find(key)
            if root not in roots:
                roots.add(root)
        return roots

    def get_component_items(self, rep):
        items = []
        for key in self.sets:
            root = self.find(key)
            if rep == root:
                items.append(key)

        return items


def get_bounding_box(locations):
    xs, ys, zs = zip(*locations)
    return min(xs), max(xs), min(ys), max(ys), min(zs), max(zs)


min_x, max_x, min_y, max_y, min_z, max_z = get_bounding_box(locations)

inverted = set()
uf = UnionFind()
for x in range(min_x, max_x + 1):
    for y in range(min_y, max_y + 1):
        for z in range(min_z, max_z + 1):
            if (x, y, z) not in locations:
                uf.make_set((x, y, z))
                # There is probably a smarter way to do this
                for rep in uf.get_component_representatives():
                    for point in uf.get_component_items(rep):
                        if adjacent(x, y, z, *point):
                            uf.union((x, y, z), point)
                            break
                inverted.add((x, y, z))


internal_surface_area = 0
for rep in uf.get_component_representatives():
    cc = set(uf.get_component_items(rep))
    min_cc_x, max_cc_x, min_cc_y, max_cc_y, min_cc_z, max_cc_z = get_bounding_box(cc)
    # This component is touching the boundary, do not count it
    if (
        min_cc_x == min_x
        or max_cc_x == max_x
        or min_cc_y == min_y
        or max_cc_y == max_y
        or min_cc_z == min_z
        or max_cc_z == max_z
    ):
        continue
    internal_surface_area += get_exposed_face_count(cc)

submit(
    get_exposed_face_count(locations) - internal_surface_area,
    part="b",
    day=DAY,
    year=YEAR,
)
