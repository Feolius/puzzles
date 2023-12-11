f = open("input.txt")

input = f.read().split("\n")

rows = []
columns_without_data = {}
for i in range(len(input[0])):
    columns_without_data[i] = True

rows_without_data = {}
for i in range(len(input)):
    rows_without_data[i] = True

galaxies = []
for i, input_string in enumerate(input):
    for j, char in enumerate(input_string):
        if char == "#":
            galaxies.append((i, j))
            columns_without_data[j] = False
            rows_without_data[i] = False


distances = []
pairs = 0
for i in range(len(galaxies) - 1):
    for j in range(i + 1, len(galaxies)):
        horizontal_length = 0
        for k in range(min(galaxies[i][1], galaxies[j][1]), max(galaxies[i][1], galaxies[j][1])):
            if columns_without_data[k]:
                horizontal_length += 1000000
            else:
                horizontal_length += 1
        vertical_length = 0
        for k in range(min(galaxies[i][0], galaxies[j][0]), max(galaxies[i][0], galaxies[j][0])):
            if rows_without_data[k]:
                vertical_length += 1000000
            else:
                vertical_length += 1
        distances.append(vertical_length + horizontal_length)

print(sum(distances))
