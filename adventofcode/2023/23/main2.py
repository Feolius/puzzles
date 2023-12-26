f = open("input.txt")

adj = lambda i, j: ((i - 1, j), (i, j - 1), (i + 1, j), (i, j + 1))
slopes = ["^", "<", "v", ">"]

input = f.read().splitlines()

tiles = {}
for i, row in enumerate(input):
    for j, char in enumerate(row):
        tiles[(i, j)] = char

MAX_I = len(input) - 1
MAX_J = len(input[0]) - 1

crossings = {}

for i in range(1, MAX_I):
    for j in range(1, MAX_J):
        if tiles[(i, j)] == "#":
            continue
        neighbours = adj(i, j)
        dirs_num = 0
        for neighbour in neighbours:
            if tiles[neighbour] == "#":
                continue
            dirs_num += 1
        if dirs_num > 2:
            crossings[(i, j)] = {}

crossings[(0, 1)] = {}
crossings[(MAX_I, MAX_J - 1)] = {}


def walk_till_crossing(pos, dir, crossings, tiles):
    distance = 0
    while True:
        pos = adj(*pos)[dir]
        distance += 1
        if pos in crossings:
            return pos, distance
        backward_dir = (dir + 2) % 4
        neighbours = adj(*pos)
        for next_dir in range(4):
            if next_dir == backward_dir:
                continue
            if tiles[neighbours[next_dir]] != "#":
                dir = next_dir
                break


for pos in crossings:
    if pos == (0, 1):
        if len(crossings[pos]) != 1:
            next_crossing, distance = walk_till_crossing(pos, 2, crossings, tiles)
            crossings[pos][next_crossing] = distance
            crossings[next_crossing][pos] = distance
        continue
    if pos == (MAX_I, MAX_J - 1):
        if len(crossings[pos]) != 1:
            next_crossing, distance = walk_till_crossing(pos, 0, crossings, tiles)
            crossings[pos][next_crossing] = distance
            crossings[next_crossing][pos] = distance
        continue
    if len(crossings[pos]) == 3:
        continue
    neighbours = adj(*pos)
    for dir in range(4):
        if tiles[neighbours[dir]] == "#":
            continue
        next_crossing, distance = walk_till_crossing(pos, dir, crossings, tiles)
        crossings[pos][next_crossing] = distance
        crossings[next_crossing][pos] = distance


def get_path_length(pos, prev_pos, crossings, visited):
    length = crossings[pos][prev_pos]
    visited[pos] = True
    if pos == (MAX_I, MAX_J - 1):
        return length
    next_length = 0
    for next_pos in crossings[pos]:
        if next_pos == prev_pos or next_pos in visited:
            continue
        next_length = max(next_length, get_path_length(next_pos, pos, crossings, dict(visited)))
    if next_length == 0:
        return 0
    return length + next_length




res = get_path_length(list(crossings[(0, 1)].keys())[0], (0, 1), crossings, {})
print(res)



