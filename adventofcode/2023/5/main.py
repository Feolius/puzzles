f = open("input.txt")

seeds = list(map(lambda item: int(item), f.readline().split(": ")[1].split(" ")))

maps = []
f.readline()
f.readline()
r_map = []
while True:
    line = f.readline()
    line_parts = line.rstrip().split(" ")
    if len(line_parts) == 3:
        r_map.append(list(map(lambda item: int(item), line_parts)))
    elif len(line) == 0:
        maps.append(r_map)
        break
    else:
        maps.append(r_map)
        f.readline()
        r_map = []

seed_results = []
for seed in seeds:
    seed_result = seed
    for r_map in maps:
        for shift in r_map:
            if shift[1] <= seed_result < shift[1] + shift[2]:
                seed_result = shift[0] + (seed_result - shift[1])
                break

    seed_results.append(seed_result)




print(min(seed_results))