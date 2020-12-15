from collections import deque

def part_one(filename='input.txt', preamble=25):
    numbers = list(map(int, [line for line  in open(filename)]))

    sum_lists = deque()

    for i, ni in enumerate(numbers):
        sum_lists.append([])

        if i > preamble and not any([ni in summand for summand in sum_lists]):
            return ni

        if len(sum_lists) > preamble:
            sum_lists.popleft()

        # TODO: Since this is looking ahead, you could probably devise an input
        # for which this fails, but it worked, so I guess I got lucky
        for nj in numbers[i+1:i+preamble]:
            if ni != nj:
                sum_lists[-1].append(ni+nj)



print(f'Part One: {part_one()}')

def part_two(filename='input.txt', preamble=25):
    target = part_one(filename, preamble)

    numbers = list(map(int, [line for line  in open(filename)]))

    contiguous_block = deque()
    for number in numbers:
        contiguous_block.append(number)
        current_sum = sum(contiguous_block)

        while current_sum > target:
            contiguous_block.popleft()
            current_sum = sum(contiguous_block)

        if current_sum == target and len(contiguous_block) > 1:
            return min(contiguous_block) + max(contiguous_block)

print(f'Part Two: {part_two()}')
