
def part_one(filename='input.txt'):
    group = set()
    summand = 0
    for line in open(filename):
        line = line.strip()
        
        if len(line) == 0:
            summand += len(group)
            group = set()
        else:
            for character in line:
                group.add(character)
        
    summand += len(group)

    return summand

print(f'Part One: {part_one()}')


def part_two(filename='input.txt'):
    group = None
    summand = 0
    for line in open(filename):
        line = line.strip()
        
        if len(line) == 0:
            summand += len(group)
            group = None
        else:
            answers = set()
            for character in line:
                answers.add(character)
            group = group.intersection(answers) if group is not None else answers
        
    summand += len(group)

    return summand

print(f'Part Two: {part_two()}')