import sys
from aocd import get_data

data = get_data(day=3, year=2022).split("\n")

summand = 0
zero_point = ord('a') - 1

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
    
print(f'Part One: {summand}')

summand = 0
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
print(f'Part Two: {summand}')
