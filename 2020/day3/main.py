from pathlib import Path


def part_one(filename='input.txt', slope=[3, 1], symbol='#'):
    grid = Path(filename).read_text().split('\n')
    
    height = len(grid)
    width = len(grid[0]) if height > 0 else 0
    
    hit_count = 0
    row = 0
    col = 0
    
    while row < height:
        if grid[row][col] == symbol:
            hit_count +=1
        col += slope[0]
        if col >= width:
            col -= width
        row += slope[1]

    return hit_count

print(f'Part One: {part_one()}')

def part_two(filename='input.txt', slopes=[[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]):
    product = 1
    for slope in slopes:
        product *= part_one(filename, slope)
    return product

print(f'Part Two: {part_two()}')