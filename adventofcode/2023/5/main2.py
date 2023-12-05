import time
start_time = time.time()
f = open("input.txt")
seeds_input = list(map(lambda item: int(item), f.readline().split(": ")[1].split(" ")))

seed_segments = []
for i in range(0, len(seeds_input), 2):
    seed_segments.append((seeds_input[i], seeds_input[i] + seeds_input[i + 1] - 1))


seed_segments.sort(key=lambda item: item[0])


maps = []
f.readline()
f.readline()
r_map = []
while True:
    line = f.readline()
    line_parts = line.rstrip().split(" ")
    if len(line_parts) == 3:
        r_map.append(list(map(lambda item: int(item), line_parts)))
    elif len(line) == 0:
        r_map.sort(key=lambda item: item[1])
        maps.append(r_map)
        break
    else:
        r_map.sort(key=lambda item: item[1])
        maps.append(r_map)
        f.readline()
        r_map = []


def segments_transformer(segments, r_map):
    r_map_i = 0
    segment_i = 0
    new_segments = []
    scan_pointer = segments[0][0]
    while True:
        if scan_pointer > segments[-1][1]:
            break
        if scan_pointer > segments[segment_i][1]:
            segment_i += 1
            scan_pointer = segments[segment_i][0]
            continue
        if r_map_i < len(r_map):
            transition_segment = (r_map[r_map_i][1], r_map[r_map_i][1] + r_map[r_map_i][2] - 1)
            transition_segment_l = transition_segment[0]
            transition_segment_r = transition_segment[1]
            shift = r_map[r_map_i][0] - r_map[r_map_i][1]
        else:
            transition_segment_l = transition_segment_r = segments[-1][1] + 1
            shift = 0
        if scan_pointer > transition_segment_r:
            r_map_i += 1
            continue

        segment = segments[segment_i]
        if transition_segment_l <= scan_pointer <= transition_segment_r:
            right_border_candidate = min(segment[1], transition_segment_r)
            new_segments.append((scan_pointer + shift, right_border_candidate + shift))
            scan_pointer = right_border_candidate + 1
            continue
        right_border_candidate = segment[1]
        if right_border_candidate < transition_segment_l:
            new_segments.append((scan_pointer, right_border_candidate))
            scan_pointer = right_border_candidate + 1
            continue
        else:
            new_segments.append((scan_pointer, transition_segment_l - 1))
            scan_pointer = transition_segment_l
            continue

    new_segments.sort(key=lambda item: item[0])
    return new_segments


segments = seed_segments
for r_map in maps:
    segments = segments_transformer(segments, r_map)


print(segments[0][0])
print("--- %s seconds ---" % (time.time() - start_time))