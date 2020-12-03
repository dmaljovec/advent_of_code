from pathlib import Path


def part_one(filename='input.txt', target=2020):
    """Satisfies part one of day one by first sorting the input rows so we can
    avoid the worst case O(n**2). We incur O(n log n) to do the sort followed by
    a brute force search with short circuiting if the sum exceeds our target.
    This is possible since we know in sorted order, only larger values will
    follow.
    
    Note, we assume only one valid solution in the given file. If more than one,
    there is no guarantee which will be returned.

    Parameters
    ----------
    filename : str, optional
        The file to parse as input will contain one integer per line,
        by default 'input.txt'
    target : int, optional
        The target sum we want to reach, by default 2020

    Returns
    -------
    int
       The product of the two integers that sum to the target value 

    Raises
    ------
    Exception
        Probably overkill, but I wanted to know if my code was failing to find
        a solution. Also, I could have looked for a more appropriate exception
        than the base one.
    """

    items = sorted(map(int, Path(filename).read_text().split()))
    count = len(items)

    iterations = 0

    for i in range(count):
        for j in range(i+1, count):
            summand = items[i] + items[j]
            iterations += 1
            if summand > target:
                break
            elif summand == target:
                print(f'Iterations: {iterations} Size: {count}')
                return items[i]*items[j]

    raise Exception('No solution!')


print(f'Part One: {part_one()}')


def part_two(filename='input.txt', target=2020):
    items = sorted(map(int, Path(filename).read_text().split()))
    count = len(items)

    iterations = 0

    for i in range(count):
        for j in range(i+1, count):
            partial_summand = items[i] + items[j]
            if partial_summand > target:
                iterations += 1
                break
            for k in range(j+1, count):
                summand = partial_summand + items[k]
                iterations += 1
                if summand > target:
                    break
                elif summand == target:
                    print(f'Iterations: {iterations} Size: {count}')
                    return items[i]*items[j]*items[k]

    raise Exception('No solution!')


print(f'Part Two: {part_two()}')
