from heapq import heappush, heappop
import math

f = open("input.txt")

input_rows = f.read().splitlines()

data = {}
for i, input_row in enumerate(input_rows):
    row = []
    for j, char in enumerate(input_row):
        data[(i, j)] = int(char)

MAX_I = len(input_rows) - 1
MAX_J = len(input_rows[0]) - 1

neighbours = lambda i, j: ((i - 1, j), (i, j - 1), (i + 1, j), (i, j + 1))

queue = []
heappush(queue, (0, (0, 0), 3, 0))
top = {}
while queue:
    item = heappop(queue)
    if item[1][0] == MAX_I and item[1][1] == MAX_J:
        print(item[0])
        break
    top_key = (item[1], item[2], item[3])
    last_dir = item[2]
    if top_key in top and top[top_key] <= item[0]:
        continue
    top[top_key] = item[0]
    current_neighbours = neighbours(*item[1])
    dirs = [(last_dir - 1) % 4, last_dir, (last_dir + 1) % 4]
    for dir_i, dir in enumerate(dirs):
        neighbour = current_neighbours[dir]
        if neighbour not in data:
            continue
        distance = 1
        if dir_i % 2 == 1:
            if item[3] < 3:
                distance = item[3] + 1
            else:
                continue
        if (neighbour, dir, distance) not in top or top[(neighbour, dir, distance)] < item[0]:
            heappush(queue, (item[0] + data[neighbour], neighbour, dir, distance))







