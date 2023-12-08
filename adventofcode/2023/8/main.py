f = open("input.txt")

input = f.read().split("\n")
commands = input[0]

nodes = {}
for i in range(2, len(input)):
    dest, LR = input[i].split(" = ")
    LR = LR.lstrip("(")
    LR = LR.rstrip(")")
    L, R = LR.split(", ")
    nodes[dest] = {
        "L": L,
        "R": R
    }



steps = 0
current = nodes["AAA"]
while True:
    for c in commands:
        steps += 1
        dest = current[c]
        if dest == "ZZZ":
            print(steps)
            break
        current = nodes[current[c]]
    else:
        continue
    break

