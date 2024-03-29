import sys
from aocd import get_data, submit

data = get_data(day=3, year=2022).split("\n")
zero_point = ord('a') - 1

summand = 0
for rucksack in data:
    midpoint = len(rucksack) // 2
    intersection = set(rucksack[:midpoint]) & set(rucksack[midpoint:])
    if len(intersection) != 1:
        print('Something went wrong')
        sys.exit(1)
    letter = intersection.pop()
    if letter == letter.upper():
        offset = 26
        letter = letter.lower()
    else:
        offset = 0
    summand += ord(letter) - zero_point + offset
    
submit(summand, part="a", day=3, year=2022)

summand = 0
# Iterating in bunches of 3 at a time
# Stolen from Stack Overflow: https://stackoverflow.com/a/3415151/11580262
for elf1, elf2, elf3 in zip(*[iter(data)]*3):
    intersection = set(elf1) & set(elf2) & set(elf3)
    if len(intersection) != 1:
        print('Something went wrong')
        sys.exit(1)
    letter = intersection.pop()
    if letter == letter.upper():
        offset = 26
        letter = letter.lower()
    else:
        offset = 0
    summand += ord(letter) - zero_point + offset

submit(summand, part="b", day=3, year=2022)
