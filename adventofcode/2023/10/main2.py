f = open("input.txt")

input = f.read().split("\n")

tiles = []
s_i = None
s_j = None
for i, input_string in enumerate(input):
    tiles_row = []
    for j, char in enumerate(input_string):
        tile = {
            "top": False,
            "bottom": False,
            "left": False,
            "right": False,
            "char": char,
            "cycle": False
        }
        if char == "|":
            tile["top"] = True
            tile["bottom"] = True
        elif char == "-":
            tile["right"] = True
            tile["left"] = True
        elif char == "L":
            tile["top"] = True
            tile["right"] = True
        elif char == "J":
            tile["top"] = True
            tile["left"] = True
        elif char == "7":
            tile["bottom"] = True
            tile["left"] = True
        elif char == "F":
            tile["bottom"] = True
            tile["right"] = True
        elif char == "S":
            s_i = i
            s_j = j
        tiles_row.append(tile)
    tiles.append(tiles_row)


MAX_I = len(tiles) - 1
MAX_J = len(tiles[0]) - 1

directions = ("top", "left", "bottom", "right")

start_end_cords = []
s_directions = []
for direction in directions:
    if direction == "top":
        if s_i == 0:
            continue
        if tiles[s_i - 1][s_j]["bottom"]:
            start_end_cords.append([s_i - 1, s_j])
            s_directions.append(direction)
            continue
    elif direction == "left":
        if s_j == 0:
            continue
        if tiles[s_i][s_j - 1]["right"]:
            start_end_cords.append([s_i, s_j - 1])
            s_directions.append(direction)
            continue
    elif direction == "bottom":
        if s_i == MAX_I:
            continue
        if tiles[s_i + 1][s_j]["top"]:
            start_end_cords.append([s_i + 1, s_j])
            s_directions.append(direction)
            continue
    else:
        if s_j == MAX_J:
            raise Exception("Cannot find start-end position")
        if tiles[s_i][s_j + 1]["left"]:
            start_end_cords.append([s_i, s_j + 1])
            s_directions.append(direction)
            continue
        raise Exception("Cannot find start-end position")


if s_directions[0] == "top" and s_directions[1] == "bottom":
    tiles[s_i][s_j]["char"] = "|"
    go_from = "bottom"
elif s_directions[0] == "left" and s_directions[1] == "right":
    tiles[s_i][s_j]["char"] = "-"
    go_from = "right"
elif s_directions[0] == "top" and s_directions[1] == "right":
    tiles[s_i][s_j]["char"] = "L"
    go_from = "bottom"
elif s_directions[0] == "top" and s_directions[1] == "left":
    tiles[s_i][s_j]["char"] = "J"
    go_from = "bottom"
elif s_directions[0] == "left" and s_directions[1] == "bottom":
    tiles[s_i][s_j]["char"] = "7"
    go_from = "right"
else:
    tiles[s_i][s_j]["char"] = "F"
    go_from = "top"



path_count = 0

cords = start_end_cords[0]
while True:
    path_count += 1
    tile = tiles[cords[0]][cords[1]]
    tile["cycle"] = True
    if cords[0] == start_end_cords[1][0] and cords[1] == start_end_cords[1][1]:
        break
    for direction in directions:
        if direction == go_from:
            continue
        if tile[direction]:
            if direction == "top":
                cords[0] = cords[0] - 1
                go_from = "bottom"
                break
            elif direction == "bottom":
                cords[0] = cords[0] + 1
                go_from = "top"
                break
            elif direction == "left":
                cords[1] = cords[1] - 1
                go_from = "right"
                break
            else:
                cords[1] = cords[1] + 1
                go_from = "left"
                break


corners_cycle_change_map = {
    "L": {
        "J": False,
        "7": True,
    },
    "F": {
        "7": False,
        "J": True
    }
}

count = 0
for i in range(len(tiles)):
    tiles_row = tiles[i]
    in_cycle = False
    prev_corner = None
    for j in range(len(tiles_row)):
        if i == s_i and j == s_j:
            continue
        tile = tiles[i][j]
        if not tile["cycle"] and in_cycle:
            count += 1
            continue
        if tile["cycle"]:
            if tile["char"] == "-":
                continue
            if tile["char"] == "|":
                in_cycle = not in_cycle
                continue
            if prev_corner is None:
                prev_corner = tile["char"]
                continue
            else:
                if corners_cycle_change_map[prev_corner][tile["char"]]:
                    in_cycle = not in_cycle
                prev_corner = None






print(count)

