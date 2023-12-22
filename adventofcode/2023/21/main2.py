import json

f = open("input.txt")

input = f.read().splitlines()

filled = 7520
first_sum = False
iter_num = 202300
for n in range(0, iter_num):
    if first_sum:
        filled += 4 * n * 7457
    else:
        filled += 4 * n * 7520
    first_sum = not first_sum


diagonals = iter_num * 943 + (iter_num - 1) * 6611 + iter_num * 950 + (iter_num - 1) * 6587 + iter_num * 965 + (iter_num - 1) * 6607 + iter_num * 948 + (iter_num - 1) * 6587
mains = 5678 + 5678 + 5674 + 5674
# this is result
res = filled + diagonals + mains


adj = lambda x, y: ((x + 1, y), (x, y - 1), (x - 1, y), (x, y + 1))

SQUARE_SIDE = len(input)
SHIFT = (SQUARE_SIDE - 1) // 2

field = {}
positions = {}
for i, row in enumerate(input):
    for j, char in enumerate(row):
        x = j - SHIFT
        y = i - SHIFT
        if char == "S":
            positions[(x, y)] = True
            char = "."
        field[(x, y)] = char


def field_transition(coordinates):
    return (coordinates[0] + SHIFT) % SQUARE_SIDE - SHIFT, (coordinates[1] + SHIFT) % SQUARE_SIDE - SHIFT


def iteration(positions, field):
    next_positions = {}
    for pos in positions:
        neighbours = adj(*pos)
        for d in range(4):
            field_coordinates = field_transition(neighbours[d])
            if field[field_coordinates] != "#":
                next_positions[neighbours[d]] = True
    return next_positions


for i in range(524 + 65):
    positions = iteration(positions, field)
    print(i)

result = open("result4.txt", "w")
result.writelines([str(pos[0]) + " " + str(pos[1]) + "\n" for pos in positions])

# result = open("result4.txt")
# result_rows = result.read().splitlines()
# positions = {}
# for result_row in result_rows:
#     x, y = result_row.split(" ")
#     positions[(int(x), int(y))] = True





# out = open("out.txt", "w")
# for y in range(196, 328):
#     line = []
#     for x in range(-65, 66):
#         if (x, y) not in positions:
#             field_coordinates = field_transition((x, y))
#             line.append(field[field_coordinates])
#         else:
#             line.append("O")
#     out.write("".join(line))
#     out.write("\n")


def print_square(i, j):
    out = open("out " + str(i) + " " + str(j) + ".txt", "w")
    for y in range(i * 131 - 65, i * 131 + 66):
        line = []
        for x in range(j * 131 - 65, j * 131 + 66):
            if (x, y) not in positions:
                field_coordinates = field_transition((x, y))
                line.append(field[field_coordinates])
            else:
                line.append("O")
        out.write("".join(line))
        out.write("\n")

# for n in range(-4,5):
#     for m in range(-4, 5):
#         print_square(n, m)

print_square(-1, 1)
print(len(positions))
