from functools import cmp_to_key

f = open("input.txt")

input = f.read().splitlines()

input_bricks = []
for input_row in input:
    start, end = input_row.split("~")
    s_x, s_y, s_z = start.split(",")
    e_x, e_y, e_z = end.split(",")
    input_bricks.append(((int(s_x), int(s_y), int(s_z)), (int(e_x), int(e_y), int(e_z))))

input_bricks.sort(key=lambda b: b[0][2])

max_x = 0
max_y = 0
max_z = 0
for brick in input_bricks:
    max_x = max(max_x, brick[0][0], brick[1][0])
    max_y = max(max_y, brick[0][1], brick[1][1])
    max_z = max(max_z, brick[0][2], brick[1][2])

occupied = {}
for x in range(max_x + 1):
    for y in range(max_y + 1):
        occupied[(x, y, 0)] = ((x, y, 0), (x, y, 0))


def get_next_available_z(point, occupied):
    z = point[2]
    while (point[0], point[1], z - 1) not in occupied:
        z -= 1
    return z


bricks = []
for brick in input_bricks:
    if brick[0][2] != brick[1][2]:
        z = get_next_available_z(brick[0], occupied)
        new_brick = ((brick[0][0], brick[0][1], z), (brick[0][0], brick[0][1], z + brick[1][2] - brick[0][2]))
        for i in range(new_brick[0][2], new_brick[1][2] + 1):
            occupied[(new_brick[0][0], new_brick[0][1], i)] = new_brick
    elif brick[0][1] != brick[1][1]:
        z = 0
        for i in range(brick[0][1], brick[1][1] + 1):
            z = max(z, get_next_available_z((brick[0][0], i, brick[0][2]), occupied))
        new_brick = ((brick[0][0], brick[0][1], z), (brick[1][0], brick[1][1], z))
        for i in range(new_brick[0][1], new_brick[1][1] + 1):
            occupied[(new_brick[0][0], i, z)] = new_brick
    else:
        z = 0
        for i in range(brick[0][0], brick[1][0] + 1):
            z = max(z, get_next_available_z((i, brick[0][1], brick[0][2]), occupied))
        new_brick = ((brick[0][0], brick[0][1], z), (brick[1][0], brick[1][1], z))
        for i in range(new_brick[0][0], new_brick[1][0] + 1):
            occupied[(i, new_brick[0][1], z)] = new_brick
    bricks.append(new_brick)

max_z = 0
for brick in bricks:
    max_z = max(max_z, brick[0][2], brick[1][2])

disintegrated = []
for z in range(2, max_z + 2):
    if z == max_z + 1:
        print(1)
    bricks_supported = {}
    bricks_supports = {}
    for x in range(max_x + 1):
        for y in range(max_y + 1):
            if (x, y, z - 1) in occupied:
                brick_support = occupied[(x, y, z - 1)]
                if brick_support not in bricks_supports:
                    bricks_supports[brick_support] = []
                if (x, y, z) in occupied:
                    if occupied[(x, y, z - 1)] == occupied[(x, y, z)]:
                        del bricks_supports[brick_support]
                        continue
                    brick = occupied[(x, y, z)]
                    if brick not in bricks_supported:
                        bricks_supported[brick] = {}
                    bricks_supported[brick][brick_support] = True
                    bricks_supports[brick_support].append(brick)
    for brick_supported in bricks_supported:
        if len(bricks_supported[brick_supported]) == 1:
            brick_support = next(iter(bricks_supported[brick_supported]))
            if brick_support in bricks_supports:
                del bricks_supports[brick_support]
    for brick_support in bricks_supports:
        disintegrated.append(brick_support)

print(len(disintegrated))
