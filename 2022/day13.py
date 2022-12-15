from aocd import get_data, submit
import json
from functools import cmp_to_key


data = get_data(day=13, year=2022).split("\n\n")


def compare(left, right):
    if isinstance(left, int) and isinstance(right, int):
        if left < right:
            return -1
        elif left == right:
            return 0
        else:
            return 1
    elif isinstance(left, list) and isinstance(right, list):
        for sub_left, sub_right in zip(left, right):
            result = compare(sub_left, sub_right)
            if result:
                return result
        if len(left) < len(right):
            return -1
        elif len(left) == len(right):
            return 0
        else:
            return 1
    elif isinstance(left, int):
        return compare([left], right)
    elif isinstance(right, int):
        return compare(left, [right])


summand = 0
for i, pair in enumerate(data, 1):
    left, right = map(json.loads, pair.split("\n"))
    if compare(left, right) < 0:
        summand += i

submit(summand, part="a", day=13, year=2022)

dividers = [[[2]], [[6]]]
data = get_data(day=13, year=2022).replace("\n\n", "\n").split("\n")
packets = list(map(json.loads, data))
packets.extend(dividers)
packets.sort(key=cmp_to_key(compare))

product = 1
for i, p in enumerate(packets, 1):
    if p in dividers:
        product *= i

submit(product, part="b", day=13, year=2022)
