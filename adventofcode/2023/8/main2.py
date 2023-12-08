f = open("input.txt")

input = f.read().split("\n")
commands = input[0]

a_dests = []
nodes = {}
for i in range(2, len(input)):
    dest, LR = input[i].split(" = ")
    LR = LR.lstrip("(")
    LR = LR.rstrip(")")
    L, R = LR.split(", ")
    if dest[2] == "A":
        a_dests.append(dest)
    nodes[dest] = {
        "L": L,
        "R": R
    }


a_dests_steps = {}
for a_dest in a_dests:
    steps = 0
    current = nodes[a_dest]
    while True:
        for c in commands:
            steps += 1
            dest = current[c]
            if dest[2] == "Z":
                a_dests_steps[a_dest] = steps
                break
            current = nodes[current[c]]
        else:
            continue
        break

print(a_dests_steps)
