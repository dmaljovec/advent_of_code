
import re

def get_seat_id(seat):
    marker = re.search('L|R', seat).start()

    row_bounds = [0, 2**marker]
    col_bounds = [0, 2**(len(seat)-marker)]
    
    for bsp, dim_bounds in [(seat[:marker], row_bounds), (seat[marker:], col_bounds)]:
        for i in bsp:
            if i in 'FL':
                dim_bounds[1] -= (1 + dim_bounds[1] - dim_bounds[0]) // 2
            elif i in 'BR':
                dim_bounds[0] += (1 + dim_bounds[1] - dim_bounds[0]) // 2
        
    return row_bounds[0] * 8 + col_bounds[0]
    

def part_one(filename="input.txt"):
    
    seats = [line.strip() for line in open(filename)]
    
    return max(map(get_seat_id, seats))

print(f'Part One: {part_one()}')

def part_two(filename="input.txt"):
    seats = [line.strip() for line in open(filename)]
    ids = sorted(map(get_seat_id, seats))
    last_seen = ids[0]
    for seat in ids[1:]:
        if last_seen + 1 != seat:
            return last_seen + 1
        last_seen = seat
    
print(f'Part Two: {part_two()}')