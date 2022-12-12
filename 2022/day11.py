from aocd import get_data, submit
from dataclasses import dataclass
from typing import Callable
from functools import total_ordering, partial
from copy import deepcopy
from time import time
from collections import deque

monkey_business = get_data(day=11, year=2022).split("\n\n")


@total_ordering
@dataclass
class Monkey:
    """Class for keeping track of an item in inventory."""

    number: int
    items: deque[int]
    operation: Callable[[int], int]
    divisor: int
    yes_monkey: int
    no_monkey: int
    touched: int = 0

    def inspect_item(self, relief_factor, total_divisor=None) -> (int, int):
        self.touched += 1
        item = self.items.popleft()
        new_value = self.operation(item) // relief_factor
        return (
            new_value % total_divisor if total_divisor else new_value,
            self.yes_monkey if new_value % self.divisor == 0 else self.no_monkey,
        )

    def receive_item(self, item) -> None:
        self.items.append(item)

    def __len__(self) -> int:
        return len(self.items)

    def __eq__(self, other) -> bool:
        return self.touched == other.touched

    def __lt__(self, other) -> bool:
        return self.touched < other.touched


monkeys = []
for data in monkey_business:
    lines = data.split("\n")
    number = int(lines[0].split(" ")[1].replace(":", ""))
    starting_items = deque(map(int, lines[1].split(":")[1].strip().split(", ")))
    operation = lines[2].split("=")[1].strip()

    def foo(old, operation):
        return eval(operation)

    divisor = int(lines[3].split("divisible by ")[1])
    yes = int(lines[4].split("monkey ")[1])
    no = int(lines[5].split("monkey ")[1])
    monkeys.append(
        Monkey(
            number,
            starting_items,
            partial(foo, operation=operation),
            divisor,
            yes,
            no,
        )
    )

monkeys2 = deepcopy(monkeys)


total_divisor = 1
for m in monkeys:
    total_divisor *= m.divisor


def solve(monkeys, rounds, relief_factor, total_divisor=None):

    for _ in range(rounds):
        for monkey in monkeys:
            while len(monkey):
                item, number = monkey.inspect_item(relief_factor, total_divisor)
                monkeys[number].receive_item(item)

    monkeys = sorted(monkeys, reverse=True)
    return monkeys[0].touched * monkeys[1].touched


submit(solve(monkeys, 20, 3), part="a", day=11, year=2022)
submit(solve(monkeys2, 10000, 1, total_divisor), part="b", day=11, year=2022)
