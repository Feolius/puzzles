f = open("input.txt")

input = f.read().split("\n")

rows = []

for input_str in input:
    rows.append(input_str.split(": ")[1])


res = 0
for row in rows:
    winning_row, my_row = row.split(" | ")
    winning_nums = list(filter(None, winning_row.split(" ")))
    my_nums = list(filter(None, my_row.split(" ")))
    points = 0
    for num in winning_nums:
        if num in my_nums:
            if points != 0:
                points = 2 * points
            else:
                points = 1
    res += points

print(res)