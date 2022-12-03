with open("day1.txt") as f:
    lines = [l.strip() for l in f.readlines()]

summands = []
summand = 0
for line in lines:
    if line == "":
        summands.append(summand)
        summand = 0
        continue
    summand += int(line)

summands.sort()
print(f"Part one: {summands[-1]}")
print(f"Part two: {sum(summands[-3:])}")
