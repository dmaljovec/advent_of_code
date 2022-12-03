import re

def part_one(filename='input.txt', required_fields=set(['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'])):
    count = 0
    current_passport = set()
    
    with open(filename) as file:
        for line in file:
            line = line.strip()
            if len(line) == 0:
                if len(required_fields - current_passport) == 0:
                    count += 1
                current_passport = set()
            tokens = line.split()
            for token in tokens:
                current_passport.add(token.split(':')[0])

    if len(required_fields - current_passport) == 0:
        count += 1

    return count

print(f'Part One: {part_one()}')

def validate_height(text):
    try:
        if text.endswith('cm') and 150 <= int(text.strip('cm')) <= 193:
            return True
        elif text.endswith('in') and 59 <= int(text.strip('in')) <= 76:
            return True
        else:
            return False
    except ValueError:
        return False

def part_two(filename='input.txt',
             required_fields={'byr': lambda x: 1920 <= int(x) <= 2002,
                              'iyr': lambda x: 2010 <= int(x) <= 2020,
                              'eyr': lambda x: 2020 <= int(x) <= 2030,
                              'hgt': validate_height,
                              'hcl': lambda x: re.compile("#[a-f0-9]{6}").fullmatch(x),
                              'ecl': lambda x: x in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'],
                              'pid': lambda x: re.compile("\d{9}").fullmatch(x)}):
    count = 0
    current_passport = set()
    
    with open(filename) as file:
        for line in file:
            line = line.strip()
            if len(line) == 0:
                if len(required_fields.keys() - current_passport) == 0:
                    count += 1
                current_passport = set()
            tokens = line.split()
            for token in tokens:
                key, value = token.split(':', 1)
                if key in required_fields and required_fields[key](value):
                    current_passport.add(token.split(':')[0])

    if len(required_fields.keys() - current_passport) == 0:
        count += 1

    return count

print(f'Part Two: {part_two()}')
