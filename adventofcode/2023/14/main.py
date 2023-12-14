f = open("test_input.txt")

input_rows = f.read().split("\n")

data_transp = [[] for _ in range(len(input_rows[0]))]
for row in input_rows:
    for j, char in enumerate(row):
        data_transp[j].append(char)


data_sloped = []
sum = 0
for row in data_transp:
    row_length = len(row)
    sloped_row = ["." for _ in range(row_length)]
    available_i = 0
    for i, char in enumerate(row):
        if char == '#':
            available_i = i + 1
            sloped_row[i] = '#'
            continue
        if char == 'O':
            sloped_row[available_i] = '0'
            sum += row_length - available_i
            available_i += 1
    data_sloped.append(sloped_row)


print(sum)