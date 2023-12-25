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


def fall_brick(brick):
    if brick[0][2] != brick[1][2]:
        z = get_next_available_z(brick[0], occupied)
    elif brick[0][1] != brick[1][1]:
        z = 0
        for i in range(brick[0][1], brick[1][1] + 1):
            z = max(z, get_next_available_z((brick[0][0], i, brick[0][2]), occupied))
    else:
        z = 0
        for i in range(brick[0][0], brick[1][0] + 1):
            z = max(z, get_next_available_z((i, brick[0][1], brick[0][2]), occupied))
    return z


def remove_brick(brick, points_to_restore):
    if brick[0][2] != brick[1][2]:
        for i in range(brick[0][2], brick[1][2] + 1):
            del occupied[(brick[0][0], brick[0][1], i)]
            points_to_restore[(brick[0][0], brick[0][1], i)] = brick
    elif brick[0][1] != brick[1][1]:
        for i in range(brick[0][1], brick[1][1] + 1):
            del occupied[(brick[0][0], i, brick[0][2])]
            points_to_restore[(brick[0][0], i, brick[0][2])] = brick
    else:
        for i in range(brick[0][0], brick[1][0] + 1):
            del occupied[(i, brick[0][1], brick[0][2])]
            points_to_restore[(i, brick[0][1], brick[0][2])] = brick

results = {}
for i, brick in enumerate(bricks):
    points_to_restore = {}
    remove_brick(brick, points_to_restore)
    count = 0
    for j, test_brick in enumerate(bricks):
        if test_brick == brick:
            continue
        z = fall_brick(test_brick)
        if z != test_brick[0][2]:
            count += 1
            remove_brick(test_brick, points_to_restore)
    results[brick] = count
    for point in points_to_restore:
        occupied[point] = points_to_restore[point]

res = 0
for brick in results:
    res += results[brick]
print(res)


