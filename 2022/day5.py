from aocd import get_data, submit
import re
import copy

columns, moves = get_data(day=5, year=2022).split("\n\n")
columns = reversed(columns.split('\n'))
names = next(columns)
stacks = [[] for v in names.split(' ') if v]

for row in columns:
    # I don't love it, but for simple cases, SO suggests chaining replaces together: 
    # https://stackoverflow.com/questions/3411771/best-way-to-replace-multiple-characters-in-a-string
    # The goal is to get a simplified string representation of a row of data without extra [ ] characters
    # once the replacements are done, every other character will represent a valid placement hence the [::2]
    row = row.replace('    ', ' [ ]').replace('[','').replace(']','')[::2]

    for i, col in enumerate(row):
        if col != ' ':
            stacks[i].append(col)

stacks1 = stacks
stacks2 = copy.deepcopy(stacks)

moves = moves.split('\n')
for move in moves:
    match = re.match('move (\d+) from (\d+) to (\d+)', move)
    count, source, destination = map(int, match.groups())
    stacks2[destination-1].extend(stacks2[source-1][-count:])
    stacks2[source-1] = stacks2[source-1][:-count]
    for _ in range(count):
        stacks1[destination-1].append(stacks1[source-1].pop())

submit(''.join([s[-1] for s in stacks1]), part="a", day=5, year=2022)
submit(''.join([s[-1] for s in stacks2]), part="b", day=5, year=2022)
