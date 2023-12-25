from functools import cmp_to_key

f = open("input.txt")

input = f.read().splitlines()

input_bricks = []
for input_row in input:
    input_parts = input_row.split()
    label = None
    if len(input_parts) == 2:
        input_row = input_parts[0]
        label = input_parts[1]
    start, end = input_row.split("~")
    s_x, s_y, s_z = start.split(",")
    e_x, e_y, e_z = end.split(",")
    if label is None:
        input_bricks.append(((int(s_x), int(s_y), int(s_z)), (int(e_x), int(e_y), int(e_z))))
    else:
        input_bricks.append(((int(s_x), int(s_y), int(s_z)), (int(e_x), int(e_y), int(e_z)), label))



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
        if len(brick) == 2:
            new_brick = ((brick[0][0], brick[0][1], z), (brick[0][0], brick[0][1], z + brick[1][2] - brick[0][2]))
        else:
            new_brick = ((brick[0][0], brick[0][1], z), (brick[0][0], brick[0][1], z + brick[1][2] - brick[0][2]), brick[2])
        for i in range(new_brick[0][2], new_brick[1][2] + 1):
            occupied[(new_brick[0][0], new_brick[0][1], i)] = new_brick
    elif brick[0][1] != brick[1][1]:
        z = 0
        for i in range(brick[0][1], brick[1][1] + 1):
            z = max(z, get_next_available_z((brick[0][0], i, brick[0][2]), occupied))
        if len(brick) == 2:
            new_brick = ((brick[0][0], brick[0][1], z), (brick[1][0], brick[1][1], z))
        else:
            new_brick = ((brick[0][0], brick[0][1], z), (brick[1][0], brick[1][1], z), brick[2])
        for i in range(new_brick[0][1], new_brick[1][1] + 1):
            occupied[(new_brick[0][0], i, z)] = new_brick
    else:
        z = 0
        for i in range(brick[0][0], brick[1][0] + 1):
            z = max(z, get_next_available_z((i, brick[0][1], brick[0][2]), occupied))
        if len(brick) == 2:
            new_brick = ((brick[0][0], brick[0][1], z), (brick[1][0], brick[1][1], z))
        else:
            new_brick = ((brick[0][0], brick[0][1], z), (brick[1][0], brick[1][1], z), brick[2])
        for i in range(new_brick[0][0], new_brick[1][0] + 1):
            occupied[(i, new_brick[0][1], z)] = new_brick
    bricks.append(new_brick)

max_z = 0
for brick in bricks:
    max_z = max(max_z, brick[0][2], brick[1][2])

results = {}
# start -> dest -> through -> True
paths_from_start = {}
# dest -> through -> True
dests_through = {}


def merge_paths_and_calc_res(brick):
    if brick not in paths_from_start:
        results[brick] = 0
        return
    if brick in results:
        return
    res = 0
    while True:
        dest_can_merge = None

        for dest in paths_from_start[brick]:
            for through in dests_through[dest]:
                if through not in paths_from_start[brick][dest]:
                    break
            else:
                dest_can_merge = dest
                break
        if dest_can_merge is None:
            break
        res += results[dest_can_merge] + 1

        if dest_can_merge in paths_from_start:
            for dest in paths_from_start[dest_can_merge]:
                if dest not in paths_from_start[brick]:
                    paths_from_start[brick][dest] = {}
                for through in paths_from_start[dest_can_merge][dest]:
                    paths_from_start[brick][dest][through] = True
            del paths_from_start[dest_can_merge]
        del paths_from_start[brick][dest_can_merge]
    results[brick] = res


def extend_paths(brick):
    for through in dests_through[brick]:
        if through not in paths_from_start:
            paths_from_start[through] = {}
        paths_from_start[through][brick] = {
            through: True
        }


for z in range(max_z, 0, -1):
    bricks = {}
    layer_dests_through = {}
    for x in range(max_x + 1):
        for y in range(max_y + 1):
            if (x, y, z - 1) in occupied:
                brick_support = occupied[(x, y, z - 1)]
                if (x, y, z) in occupied:
                    brick = occupied[(x, y, z)]
                    bricks[brick] = True
                    if occupied[(x, y, z - 1)] == occupied[(x, y, z)]:
                        continue
                    if brick not in layer_dests_through:
                        layer_dests_through[brick] = {}
                    if brick not in dests_through:
                        dests_through[brick] = {}
                    layer_dests_through[brick][brick_support] = True
                    dests_through[brick][brick_support] = True
    for brick in bricks:
        merge_paths_and_calc_res(brick)
    for brick in layer_dests_through:
        extend_paths(brick)



res = 0
for brick in results:
    res += results[brick]
print(res)
