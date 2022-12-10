from aocd import get_data, submit

data = get_data(day=9, year=2022).split("\n")


def move_tail(head, tail):
    delta = [head[0] - tail[0], head[1] - tail[1]]

    if max(map(abs, delta)) <= 1:
        return tail

    if delta[0] >= 1:
        tail[0] += 1
    elif delta[0] <= -1:
        tail[0] -= 1

    if delta[1] >= 1:
        tail[1] += 1
    elif delta[1] <= -1:
        tail[1] -= 1

    return tail


def parse_instruction(line):
    direction, count = line.split(" ")
    match direction:
        case "U":
            vector = [0, 1]
        case "L":
            vector = [-1, 0]
        case "D":
            vector = [0, -1]
        case "R":
            vector = [1, 0]
    count = int(count)
    return vector, count


def solve(instructions, num_knots):
    knots = []
    for i in range(num_knots):
        knots.append([0, 0])
    tail_positions = set()
    tail_positions.add(tuple(knots[-1]))

    for line in instructions:
        vector, count = parse_instruction(line)
        while count:
            knots[0][0] += vector[0]
            knots[0][1] += vector[1]
            for i in range(1, len(knots)):
                knots[i] = move_tail(knots[i - 1], knots[i])
            tail_positions.add(tuple(knots[-1]))
            count -= 1
    return len(tail_positions)


submit(solve(data, 2), part="a", day=9, year=2022)
submit(solve(data, 10), part="b", day=9, year=2022)
