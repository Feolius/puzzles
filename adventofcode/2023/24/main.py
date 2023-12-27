f = open("input.txt")

rows = f.read().splitlines()
lines = []
for row in rows:
    coords, velocities = row.split(" @ ")
    x, y, z = map(lambda item: int(item), coords.split(", "))
    vx, vy, vz = map(lambda item: int(item), velocities.split(", "))
    k = vy / vx
    b = y - k * x
    lines.append({
        "x": x,
        "y": y,
        "vx": vx,
        "vy": vy,
        "k": k,
        "b": b
    })

MIN = 200000000000000
MAX = 400000000000000
# MIN = 7
# MAX = 27

res = 0
for i in range(len(lines) - 1):
    for j in range(i + 1, len(lines)):
        line1 = lines[i]
        line2 = lines[j]
        if line1["k"] == line2["k"]:
            continue
        x = (line2["b"] - line1["b"]) / (line1["k"] - line2["k"])
        if x < MIN or x > MAX:
            continue
        if x < line1["x"] and line1["vx"] > 0:
            continue
        if x > line1["x"] and line1["vx"] < 0:
            continue
        if x < line2["x"] and line2["vx"] > 0:
            continue
        if x > line2["x"] and line2["vx"] < 0:
            continue
        y = line2["k"] * x + line2["b"]
        if y < MIN or y > MAX:
            continue
        if y < line1["y"] and line1["vy"] > 0:
            continue
        if y > line1["y"] and line1["vy"] < 0:
            continue
        if y < line2["y"] and line2["vy"] > 0:
            continue
        if y > line2["y"] and line2["vy"] < 0:
            continue
        res += 1
print(res)
