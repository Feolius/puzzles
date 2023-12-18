import math
import sys

f = open("input.txt")

input_rows = f.read().splitlines()

adj = lambda x, y: ((x + 1, y), (x, y - 1), (x - 1, y), (x, y + 1))
commands = []
for row in input_rows:
    _, _, colour = row.split(" ")
    colour = colour.lstrip("(#").rstrip(")")
    dir = int(colour[-1])
    steps = int("0x" + colour[:-1], 0)

    # dir, steps, _ = row.split(" ")
    # steps = int(steps)
    # if dir == "U":
    #     dir = 3
    # elif dir == "L":
    #     dir = 2
    # elif dir == "D":
    #     dir = 1
    # else:
    #     dir = 0

    commands.append((dir, steps))

def get_corner(next_command, command):
    corner = next_command[0] - command[0]
    if corner == 3:
        corner = -1
    elif corner == -3:
        corner = 1
    return corner

vertices = [(0, 1)]
prev = (0, 1)
for i in range(len(commands)):
    command = commands[i]
    prev_command = commands[i - 1]
    next_command = commands[(i + 1) % len(commands)]
    corner = get_corner(next_command, command)
    prev_corner = get_corner(command, prev_command)
    shift = (corner + prev_corner) // 2
    if command[0] == 0:
        vertice = (prev[0] + command[1] + shift, prev[1])
    elif command[0] == 1:
        vertice = (prev[0], prev[1] - command[1] - shift)
    elif command[0] == 2:
        vertice = (prev[0] - command[1] - shift, prev[1])
    else:
        vertice = (prev[0], prev[1] + command[1] + shift)
    vertices.append(vertice)
    prev = vertice



vertices.pop()

res = 0
for i in range(len(vertices)):
    next_i = i + 1
    if next_i >= len(vertices):
        next_i = 0
    res += (vertices[i][1] + vertices[next_i][1]) * (vertices[i][0] - vertices[next_i][0])

res = 0.5 * res

print(res)