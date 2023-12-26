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

def get_path_length(pos, dir, tiles, slopes_used):
    length = 0
    while True:
        pos = adj(*pos)[dir]
        length += 1
        if pos == (MAX_I, MAX_J - 1):
            return length
        backward_dir = (dir + 2) % 4
        possible_next_dirs = []
        neighbours = adj(*pos)
        for next_dir in range(4):
            if next_dir == backward_dir:
                continue
            if tiles[neighbours[next_dir]] == ".":
                possible_next_dirs.append(next_dir)
                continue
            if tiles[neighbours[next_dir]] == slopes[next_dir] and neighbours[next_dir] not in slopes_used:
                slopes_used[neighbours[next_dir]] = True
                possible_next_dirs.append(next_dir)
                continue
        if len(possible_next_dirs) == 0:
            return 0
        elif len(possible_next_dirs) > 1:
            next_path_length = 0
            for next_dir in possible_next_dirs:
                next_path_length = max(next_path_length, get_path_length(pos, next_dir, tiles, dict(slopes_used)))
            if next_path_length == 0:
                return 0
            return next_path_length + length
        dir = possible_next_dirs[0]


res = get_path_length((0, 1), 2, tiles, {})
print(res)



