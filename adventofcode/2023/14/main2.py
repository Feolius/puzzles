f = open("input.txt")

input_rows = f.read().split("\n")
init_data = []
for input_row in input_rows:
    row = []
    for char in input_row:
        row.append(char)
    init_data.append(row)


def data_transp(data):
    data_transp = [[] for _ in range(len(data[0]))]
    for row in data:
        for j, char in enumerate(row):
            data_transp[j].append(char)
    return data_transp


def slope(data, reverse = False):
    data_sloped = []
    for row in data:
        if reverse:
            row.reverse()
        row_length = len(row)
        sloped_row = ["." for _ in range(row_length)]
        available_i = 0
        for i, char in enumerate(row):
            if char == "#":
                available_i = i + 1
                sloped_row[i] = "#"
                continue
            if char == "O":
                sloped_row[available_i] = "O"
                available_i += 1
        if reverse:
            sloped_row.reverse()
        data_sloped.append(sloped_row)
    return data_sloped



def cycle(data):
    data = data_transp(data)
    data = slope(data)
    data = data_transp(data)
    data = slope(data)
    data = data_transp(data)
    data = slope(data, True)
    data = data_transp(data)
    data = slope(data, True)
    return data


data = init_data
cycles = 1
hashes = {}
while True:
    data = cycle(data)
    hash = str(data)
    if hash in hashes:
        print("cycle is same in iteration: " + str(cycles) + " " + str(hashes[hash]))
        break
    else:
        hashes[hash] = cycles
    cycles += 1

c = (1000000000 - 109) % 36 + 109

data = init_data
for i in range(c):
    data = cycle(data)

def calc_sum(data):
    sum = 0
    for i, row in enumerate(data):
        for char in row:
            if char == "O":
                sum += len(data) - i
    return sum


# data = cycle(init_data)
# data = cycle(data)
# data = cycle(data)
# data = cycle(data)
# data = cycle(data)
# data = cycle(data)

# data = data_transp(init_data)
# data = slope(data)
# data = data_transp(data)
print(calc_sum(data))
