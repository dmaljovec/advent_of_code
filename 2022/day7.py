from aocd import get_data, submit

THRESHOLD = 100000
LIMIT = 70000000
MIN_FREE = 30000000

lines = get_data(day=7, year=2022).split('\n')
folders = {} # this will accumulate running totals for each folder
cwd = [] # this will be a stack
folders[tuple()] = 0
for line in lines:
    match line.split(' '):
        case ['$', 'ls']:
            pass
        case ['$', 'cd', '..']:
            cwd.pop()
        case ['$', 'cd', '/']:  # ugh, it's easier to special case my root path
            cwd = []
        case ['$', 'cd', dir]:
            cwd.append(dir)
            full_path = tuple(cwd)
            if full_path not in folders:
                folders[full_path] = 0
        case ['dir', dir]:
            this_path = tuple([*cwd, dir])
            if this_path not in folders:
                folders[this_path] = 0
        case [size, file]:
            for i in range(0, len(cwd)+1):
                partial_path = tuple(cwd[:i])
                folders[partial_path] += int(size)
        case _:
            print("Oof! Baboof! You shouldn't be here. Something went wrong!")


summand = sum([value for value in folders.values() if value < THRESHOLD])
submit(summand, part="a", day=7, year=2022)

total_used = folders[tuple()]
smallest_edit = min([value for value in folders.values() if LIMIT-total_used+value > MIN_FREE])
submit(smallest_edit, part="b", day=7, year=2022)
