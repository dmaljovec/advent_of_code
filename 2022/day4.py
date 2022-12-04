from aocd import get_data, submit
import re

data = get_data(day=4, year=2022).split("\n")
count = 0
count2 = 0
for row in data:
    min1, max1, min2, max2 = map(int, re.split('-|,', row))
    # This also works for Part A, but I refactored it during Part B to condense
    # if (min1 <= min2 and max1 >= max2) or (min1 >= min2 and max1 <= max2):
    #     count += 1
    values1 = set(range(min1, max1+1))
    values2 = set(range(min2, max2+1))
    if len(values1 & values2):
        if len(values1 & values2) in [len(values1), len(values2)]:
            count += 1
        count2 += 1
submit(count, part="a", day=4, year=2022)
submit(count2, part="b", day=4, year=2022)
