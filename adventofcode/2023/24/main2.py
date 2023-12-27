f = open("input.txt")

rows = f.read().splitlines()
lines = []
for row in rows:
    coords, velocities = row.split(" @ ")
    x, y, z = map(lambda item: int(item), coords.split(", "))
    vx, vy, vz = map(lambda item: int(item), velocities.split(", "))
    lines.append({
        "x": x,
        "y": y,
        "z": z,
        "vx": vx,
        "vy": vy,
        "vz": vz
    })

for i in range(len(lines) - 2):
    for j in range(i + 1, len(lines) - 1):
        if (lines[i]["vx"] / lines[j]["vx"]) == (lines[i]["vy"] / lines[j]["vy"]) == (lines[i]["vz"] / lines[j]["vz"]):
            print(i, j)


def lines_intersect(line1, line2):
    if line1["vx"] == 0 or line2["vx"] == 0:
        return None
    ky1 = line1["vy"] / line1["vx"]
    ky2 = line2["vy"] / line2["vx"]
    if ky1 == ky2:
        return None
    by1 = line1["y"] - ky1 * line1["x"]
    by2 = line2["y"] - ky2 * line2["x"]
    ix = (by2 - by1) / (ky1 - ky2)
    if (ix < line1["x"] and line1["vx"] > 0) or (ix > line1["x"] and line1["vx"] < 0) or (ix < line2["x"] and line2["vx"] > 0) or (ix > line2["x"] and line2["vx"] < 0):
        return None
    iy = ky1 * ix + by1
    if (iy < line1["y"] and line1["vy"] > 0) or (iy > line1["y"] and line1["vy"] < 0) or (iy < line2["y"] and line2["vy"] > 0) or (iy > line2["y"] and line2["vy"] < 0):
        return None
    kz1 = line1["vz"] / line1["vx"]
    kz2 = line2["vz"] / line2["vx"]
    if kz1 == kz2:
        return None
    bz1 = line1["z"] - kz1 * line1["x"]
    bz2 = line2["z"] - kz2 * line2["x"]
    ix_z = (bz2 - bz1) / (kz1 - kz2)
    if abs(ix - ix_z) > 1:
        return None
    iz = kz1 * ix + bz1
    return ix, iy, iz

for vx in range(-300, 300):
    print(vx)
    for vy in range(-300, 300):
        for vz in range(-300, 300):
            line1 = dict(lines[1])
            line1["vx"] -= vx
            line1["vy"] -= vy
            line1["vz"] -= vz
            line2 = dict(lines[2])
            line2["vx"] -= vx
            line2["vy"] -= vy
            line2["vz"] -= vz
            i_p1 = lines_intersect(line1, line2)
            if i_p1 is None:
                continue
            line3 = dict(lines[3])
            line3["vx"] -= vx
            line3["vy"] -= vy
            line3["vz"] -= vz
            i_p2 = lines_intersect(line2, line3)
            if i_p2 is not None:
                print(i_p1, i_p2)
            if i_p2 is not None and abs(i_p1[0] - i_p2[0]) < 0.1 and abs(i_p1[1] - i_p2[1]) < 0.1 and abs(i_p1[2] - i_p2[2]) < 0.1:
                print(i_p1, i_p2)
                break


        else:
            continue
        break
    else:
        continue
    break

print(i_p1)
print(sum(i_p1))