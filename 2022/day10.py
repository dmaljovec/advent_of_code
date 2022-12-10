from aocd import get_data, submit
import textwrap

data = get_data(day=10, year=2022).split("\n")

X = 1
cycle_values = [X]

for instruction in data:
    match instruction.split(" "):
        case ["noop"]:
            cycle_values.append(X)
        case ["addx", v]:
            cycle_values.append(X)
            cycle_values.append(X)
            X += int(v)

summand = 0
for i in range(20, 221, 40):
    summand += i * cycle_values[i]
submit(summand, part="a", day=10, year=2022)

CRT = ""
for i in range(1, 241):
    col = (i - 1) % 40
    if (col - 1) <= cycle_values[i] <= (col + 1):
        CRT += "#"
    else:
        CRT += "."
print("\n".join(textwrap.wrap(CRT, 40)))

answer = input("What do you see?")

submit(answer, part="b", day=10, year=2022)
