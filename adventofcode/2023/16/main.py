import sys

f = open("input.txt")

input_strings = f.read().split("\n")

tiles = []
for input_string in input_strings:
    tiles_row = []
    for char in input_string:
        tile = {
            "char": char,
            "crossed_directions": []
        }
        tiles_row.append(tile)
    tiles.append(tiles_row)

MAX_I = len(tiles) - 1
MAX_J = len(tiles[0]) - 1

beams = {
    0: {
        0: ["right"]
    }
}

iteration = -1
while True:
    iteration += 1
    if iteration == 54:
        print("dfg")
    if not beams:
        break
    crossed_direction_changes = {}
    for beam_i in list(beams):
        for beam_j in list(beams[beam_i]):
            if beam_i < 0 or beam_i > MAX_I or beam_j < 0 or beam_j > MAX_J:
                del beams[beam_i][beam_j]
                if not beams[beam_i]:
                    del beams[beam_i]
                continue
            for current_direction in beams[beam_i][beam_j]:
                tile = tiles[beam_i][beam_j]
                if current_direction in tile["crossed_directions"]:
                    continue

                if beam_i not in crossed_direction_changes:
                    crossed_direction_changes[beam_i] = {}
                if beam_j not in crossed_direction_changes[beam_i]:
                    crossed_direction_changes[beam_i][beam_j] = []

                if current_direction not in crossed_direction_changes[beam_i][beam_j]:
                    crossed_direction_changes[beam_i][beam_j].append(current_direction)
                else:
                    print("dfgdsf")

                next_directions = [current_direction]
                if tile["char"] == "|":
                    if current_direction == "right" or current_direction == "left":
                        next_directions = ["top", "bottom"]
                elif tile["char"] == "-":
                    if current_direction == "top" or current_direction == "bottom":
                        next_directions = ["right", "left"]
                elif tile["char"] == "/":
                    if current_direction == "right":
                        next_directions = ["top"]
                    elif current_direction == "left":
                        next_directions = ["bottom"]
                    elif current_direction == "top":
                        next_directions = ["right"]
                    else:
                        next_directions = ["left"]
                elif tile["char"] == "\\":
                    if current_direction == "right":
                        next_directions = ["bottom"]
                    elif current_direction == "left":
                        next_directions = ["top"]
                    elif current_direction == "top":
                        next_directions = ["left"]
                    else:
                        next_directions = ["right"]

                for next_direction in next_directions:
                    if next_direction == "right":
                        if beam_j + 1 not in beams[beam_i]:
                            beams[beam_i][beam_j + 1] = []
                        beams[beam_i][beam_j + 1].append("right")
                    elif next_direction == "left":
                        if beam_j - 1 not in beams[beam_i]:
                            beams[beam_i][beam_j - 1] = []
                        beams[beam_i][beam_j - 1].append("left")
                    elif next_direction == "top":
                        if beam_i - 1 not in beams:
                            beams[beam_i - 1] = {}
                        if beam_j not in beams[beam_i - 1]:
                            beams[beam_i - 1][beam_j] = []
                        beams[beam_i - 1][beam_j].append("top")
                    else:
                        if beam_i + 1 not in beams:
                            beams[beam_i + 1] = {}
                        if beam_j not in beams[beam_i + 1]:
                            beams[beam_i + 1][beam_j] = []
                        beams[beam_i + 1][beam_j].append("bottom")
            del beams[beam_i][beam_j]
            if not beams[beam_i]:
                del beams[beam_i]

    for i in crossed_direction_changes:
        for j in crossed_direction_changes[i]:
            tiles[i][j]["crossed_directions"].extend(crossed_direction_changes[i][j])


res = 0
for i, tiles_row in enumerate(tiles):
    print("")
    # sys.stdout.write(str(i + 1) + " ")
    for tile in tiles_row:
        if tile["crossed_directions"]:
            res += 1
        else:
            a = 1
        if tile["char"] != ".":
            sys.stdout.write(tile["char"])
            continue
        if tile["crossed_directions"]:
            if len(tile["crossed_directions"]) > 1:
                sys.stdout.write(str(len(tile["crossed_directions"])))
            else:
                if tile["crossed_directions"][0] == "top":
                    sys.stdout.write("^")
                elif tile["crossed_directions"][0] == "bottom":
                    sys.stdout.write("v")
                elif tile["crossed_directions"][0] == "left":
                    sys.stdout.write("<")
                else:
                    sys.stdout.write(">")
        else:
            sys.stdout.write(tile["char"])

# for tiles_row in tiles:
#     print("")
#     for tile in tiles_row:
#         if tile["crossed_directions"]:
#             res += 1
#             sys.stdout.write("#")
#         else:
#             sys.stdout.write(".")

print(res)



