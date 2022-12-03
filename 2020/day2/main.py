from pathlib import Path


def part_one(filename='input.txt'):
    """[summary]

    Parameters
    ----------
    filename : str, optional
        [description], by default 'input.txt'

    Returns
    -------
    [type]
        [description]
    """

    lines = Path(filename).read_text().split('\n')
    valid_passwords = 0
    for line in lines:
        tokens = line.split()
        bounds = list(map(int, tokens[0].split('-')))
        character = tokens[1].strip(':')
        if bounds[0] <= tokens[2].count(character) <= bounds[1]:
            valid_passwords += 1

    return valid_passwords

print(f'Part One: {part_one()}')

def part_two(filename='input.txt'):
    """[summary]

    Parameters
    ----------
    filename : str, optional
        [description], by default 'input.txt'

    Returns
    -------
    [type]
        [description]
    """

    lines = Path(filename).read_text().split('\n')
    valid_passwords = 0
    for line in lines:
        tokens = line.split()
        positions = list(map(lambda x: tokens[2][int(x)-1], tokens[0].split('-')))
        character = tokens[1].strip(':')
        if positions.count(character) == 1:
            valid_passwords += 1

    return valid_passwords

print(f'Part Two: {part_two()}')