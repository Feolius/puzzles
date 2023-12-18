import math
import sys

f = open("input.txt")

input_rows = f.read().splitlines()

adj = lambda i, j: ((i - 1, j), (i, j - 1), (i + 1, j), (i, j + 1))
commands = []
for row in input_rows:
    dir, steps, colour = row.split(" ")
    if dir == "U":
        dir = 0
    elif dir == "L":
        dir = 1
    elif dir == "D":
        dir = 2
    else:
        dir = 3

    commands.append((dir, int(steps), colour))

colored = {(0, 0): ""}
current = (0, 0)
for command in commands:
    for _ in range(command[1]):
        current = adj(*current)[command[0]]
        colored[current] = command[2]

min_i = math.inf
min_j = math.inf
max_i = -math.inf
max_j = -math.inf
for current in colored:
    min_i = min(min_i, current[0])
    min_j = min(min_j, current[0])
    max_i = max(max_i, current[0])
    max_j = max(max_j, current[1])


# res = 0
# inside = False
# for i in range(min_i, max_i + 1):
#     print("")
#     for j in range(min_j, max_j + 1):
#         if (i, j) in colored:
#             sys.stdout.write("#")
#         else:
#             sys.stdout.write(".")

res = 0
inside = False
prev_corner_dir = None
corners = []
for i in range(min_i, max_i + 1):
    print("")
    for j in range(min_j, max_j + 1):
        if (i, j) in colored:
            if (i + 1, j) in colored:
                corners.append(i + 1)
            if (i - 1, j) in colored:
                corners.append(i - 1)
            if len(corners) == 2:
                if not (corners[0] - corners[1]) == 0:
                    inside = not inside
                corners = []
            sys.stdout.write("#")
            res += 1
        elif inside:
            res += 1
            sys.stdout.write("#")
        else:
            sys.stdout.write(".")


print(res)