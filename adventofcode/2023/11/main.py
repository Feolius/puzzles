f = open("test_input.txt")

input = f.read().split("\n")

rows = []
columns_without_data = {}
for i in range(len(input[0])):
    columns_without_data[i] = True

with_double_rows = []
for input_string in input:
    no_data = True
    for j, char in enumerate(input_string):
        if char == "#":
            no_data = False
            columns_without_data[j] = False
    with_double_rows.append(input_string)
    if no_data:
        with_double_rows.append(input_string)


true_data = []
for input_string in with_double_rows:
    true_data_row = []
    for j, char in enumerate(input_string):
        true_data_row.append(char)
        if columns_without_data[j]:
            true_data_row.append(char)
    true_data.append(true_data_row)

galaxies = []
for i, row in enumerate(true_data):
    for j, char in enumerate(row):
        if char == "#":
            galaxies.append((i, j))


distances = []
pairs = 0
for i in range(len(galaxies) - 1):
    for j in range(i + 1, len(galaxies)):
        distance = (max(galaxies[i][0], galaxies[j][0]) - min(galaxies[i][0], galaxies[j][0])) + (max(galaxies[i][1], galaxies[j][1]) - min(galaxies[i][1], galaxies[j][1]))
        distances.append(distance)

print(sum(distances))
