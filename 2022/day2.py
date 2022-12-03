from aocd import get_data

data = get_data(day=2, year=2022).split("\n")
decoder_ring = {
    "A": 1,
    "B": 2,
    "C": 3,
    "X": 1,
    "Y": 2,
    "Z": 3,
}

total_score = 0
for datum in data:
    them, me = datum.split(" ")
    score = decoder_ring[me]
    if decoder_ring[me] == decoder_ring[them]:
        score += 3
    elif (decoder_ring[me] - 1) == (decoder_ring[them] % 3):
        score += 6

    total_score += score

print(f"Part One: {total_score}")

modifier = {
    "X": -1,
    "Y": 0,
    "Z": 1,
}

total_score = 0
offset = ord("A")
for datum in data:
    them, outcome = datum.split(" ")
    me = chr(((ord(them) + modifier[outcome] - offset) % 3) + offset)
    score = decoder_ring[me]
    if outcome == "Y":
        score += 3
    elif outcome == "Z":
        score += 6

    total_score += score

print(f"Part Two: {total_score}")
