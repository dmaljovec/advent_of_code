def part_one(filename='input.txt'):

    accumulator = 0
    seen = set()
    lines = [line.strip().split() for line in open(filename)]

    current = 0

    while(True):
        if current in seen:
            return accumulator
        seen.add(current)

        if lines[current][0] == 'acc':
            accumulator += int(lines[current][1])
            current += 1
        elif lines[current][0] == 'jmp':
            current += int(lines[current][1])
        elif lines[current][0] == 'nop':
            current += 1

print(f'Part One: {part_one()}')

def part_two(filename='input.txt'):

    lines = [line.strip().split() for line in open(filename)]

    permutations = []
    for i, line in enumerate(lines):
        if line[0] == 'nop':
            permutations.append(lines[:i] + [('jmp', line[1])] + lines[i+1:])
        elif line[0] == 'jmp':
            permutations.append(lines[:i] + [('nop', line[1])] + lines[i+1:])

    for lines in permutations:
        current = 0
        accumulator = 0
        seen = set()

        while(True):
            if current in seen:
                break # Loop found, Not a correct solution
            seen.add(current)

            if lines[current][0] == 'acc':
                accumulator += int(lines[current][1])
                current += 1
            elif lines[current][0] == 'jmp':
                current += int(lines[current][1])
            elif lines[current][0] == 'nop':
                current += 1

            if current >= len(lines):
                return accumulator

print(f'Part Two: {part_two()}')

