f = open("input.txt")

input = f.read().splitlines()

adj = lambda i, j: ((i - 1, j), (i, j - 1), (i + 1, j), (i, j + 1))

field = {}
positions = {}
for i, row in enumerate(input):
    for j, char in enumerate(row):
        if char == "S":
            positions[(i, j)] = True
            char = "."
        field[(i, j)] = char


def iteration(positions):
    next_positions = {}
    for pos in positions:
        neighbours = adj(*pos)
        for d in range(4):
            if neighbours[d] in field and field[neighbours[d]] != "#":
                next_positions[neighbours[d]] = True
    return next_positions


for _ in range(64):
    positions = iteration(positions)


print(len(positions))
