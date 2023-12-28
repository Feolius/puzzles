import random
from heapq import heappush, heappop
f = open("input.txt")

lines = f.read().splitlines()

nodes = {}
for i, line in enumerate(lines):
    left, right = line.split(": ")
    right_parts = right.split(" ")
    if left in nodes:
        left_node = nodes[left]
    else:
        nodes[left] = {}

    for right_part in right_parts:
        if right_part not in nodes:
            nodes[right_part] = {}
        nodes[left][right_part] = i
        nodes[right_part][left] = i


def shortest_path(start, end, nodes):
    queue = []
    marked = {
        start: None
    }
    heappush(queue, (0, start, None))
    while True:
        current = heappop(queue)
        for next_node in nodes[current[1]]:
            if next_node in marked:
                continue
            marked[next_node] = {
                "prev": current[1],
                "connect": nodes[current[1]][next_node]
            }
            if next_node == end:
                break
            heappush(queue, (current[0] + 1, next_node, current[1]))
        else:
            continue
        break

    prev_name = end
    path_names = []
    while True:
        path_names.append(prev_name)
        prev = marked[prev_name]
        if prev is None:
            break
        prev_name = prev["prev"]
    return path_names


paths_found = {}
reverse_paths = {}
node_names = list(nodes.keys())
pair_connections = {}
while len(paths_found) < 4000:
    i = random.randrange(len(node_names))
    j = random.randrange(len(node_names))
    start = node_names[i]
    end = node_names[j]
    if start == end or (start, end) in paths_found or (start, end) in paths_found:
        continue
    path = shortest_path(start, end, nodes)
    if len(path) == 1:
        continue
    for k in range(len(path) - 1):
        if (path[k], path[k + 1]) in pair_connections:
            pair_connections[(path[k], path[k + 1])] += 1
        elif (path[k + 1], path[k]) in pair_connections:
            pair_connections[(path[k + 1], path[k])] += 1
        else:
            pair_connections[(path[k], path[k + 1])] = 1
    paths_found[(start, end)] = paths_found[(end, start)] = True

pair_connections_sorted = sorted(list(pair_connections.items()), key=lambda item: item[1], reverse=True)

def build_heap(start, disconnects, nodes):
    queue = []
    heap = {}
    queue.append(start)
    while queue:
        current = queue.pop()
        for next in nodes[current]:
            if (current, next) in disconnects or (next, current) in disconnects:
                continue
            if next in heap:
                continue
            heap[next] = True
            queue.append(next)
    return heap

start_node = node_names[random.randrange(len(node_names))]
disconnects = [item[0] for item in pair_connections_sorted[:3]]
heap1 = build_heap(start_node, disconnects, nodes)


res = (len(nodes) - len(heap1)) * len(heap1)

print(res)
