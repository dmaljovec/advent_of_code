from aocd import get_data, submit
import sys
from itertools import cycle


## 3213 is too low
## 3350 is too high

################################################################################
## Common bits

YEAR = 2022
DAY = 17

WIDTH = 7

moves = cycle(get_data(day=DAY, year=YEAR))
# moves = cycle(">>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>")
shapes = cycle("-+L|.")


def print_chamber(chamber, rock, max_height):
    if rock is not None:
        maximum = max(max_height, *[y for _, y in rock.locations])
    else:
        maximum = max_height
    for i in range(maximum, -1, -1):
        print("|", end="")
        for j in range(WIDTH):
            if rock is not None and (j, i) in rock.locations:
                print("@", end="")
            else:
                print(f'{"#" if chamber[i][j] else "."}', end="")
        print("|")
    print("+" + "-" * WIDTH + "+")


class Rock(object):
    def __init__(self, shape, height) -> None:
        match shape:
            case "-":
                self.locations = [
                    (2, height),
                    (3, height),
                    (4, height),
                    (5, height),
                ]
            case "+":
                self.locations = [
                    (3, height),
                    (2, height + 1),
                    (3, height + 1),
                    (4, height + 1),
                    (3, height + 2),
                ]
            case "L":
                self.locations = [
                    (2, height),
                    (3, height),
                    (4, height),
                    (4, height + 1),
                    (4, height + 2),
                ]
            case "|":
                self.locations = [
                    (2, height),
                    (2, height + 1),
                    (2, height + 2),
                    (2, height + 3),
                ]
            case ".":
                self.locations = [
                    (2, height),
                    (2, height + 1),
                    (3, height),
                    (3, height + 1),
                ]

    def translate(self, x, y) -> None:
        for i in range(len(self.locations)):
            self.locations[i] = (self.locations[i][0] + x, self.locations[i][1] + y)

    def collision(self, board, dx, dy) -> bool:
        for xi, yi in self.locations:
            new_x = xi + dx
            new_y = yi + dy
            if new_x < 0 or new_x >= WIDTH or new_y < 0 or board[new_y][new_x]:
                return True
        return False

    def lock(self, board) -> list[list[bool]]:
        for xi, yi in self.locations:
            board[yi][xi] = True
        return board


################################################################################
## Part A


def solve(count=2022):
    # The tallest piece is 4 units high plus the three units up that we start with
    # every time
    MAX_HEIGHT = count * 4 + 3

    tower_height = 0
    chamber = []
    for _ in range(MAX_HEIGHT):
        chamber.append([False for _ in range(WIDTH)])

    blocks = 0

    for j in range(count):
        rock = Rock(next(shapes), tower_height + 3)
        blocks += len(rock.locations)

        directions = cycle("hv")
        dx = 0
        dy = 0
        while not rock.collision(chamber, dx, dy) or dy == 0:
            if not rock.collision(chamber, dx, dy):
                rock.translate(dx, dy)

            match next(directions):
                case "h":
                    dy = 0
                    move = next(moves)
                    dx = -1 if move == "<" else 1
                case "v":
                    dx = 0
                    dy = -1

        chamber = rock.lock(chamber)
        for i in range(0, 5):  # four is the tallest piece
            if not any(chamber[tower_height + i]):
                tower_height = tower_height + i
                break
        covered_squares = 0
        for row in chamber:
            for col in row:
                if col:
                    covered_squares += 1
    return tower_height


submit(solve(2022), part="a", day=DAY, year=YEAR)
submit(solve(1000000000000), part="b", day=DAY, year=YEAR)

################################################################################
## Part B

# submit(None, part="b", day=DAY, year=YEAR)
