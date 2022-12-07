from aocd import get_data, submit

datastream = get_data(day=6, year=2022)

packet_marker = []
for i, character in enumerate(datastream, start=1):
    packet_marker.append(character)
    if len(set(packet_marker)) == 4:
        start_of_packet_marker = i
        break
    if len(packet_marker) == 4:
        packet_marker.pop(0)

submit(start_of_packet_marker, part="a", day=6, year=2022)

message_marker = []
for i, character in enumerate(datastream, start=1):
    message_marker.append(character)
    if len(set(message_marker)) == 14:
        start_of_message_marker = i
        break
    if len(message_marker) == 14:
        message_marker.pop(0)

submit(start_of_message_marker, part="b", day=6, year=2022)

