from aocd import get_data, submit

datastream = get_data(day=6, year=2022)

def get_first_unique(datastream, unique_size):
    marker = []
    for i, character in enumerate(datastream, start=1):
        marker.append(character)
        if len(set(marker)) == unique_size:
            return i
        if len(marker) == unique_size:
            marker.pop(0)

submit(get_first_unique(datastream, 4), part="a", day=6, year=2022)
submit(get_first_unique(datastream, 14), part="b", day=6, year=2022)
