f = open("input.txt")

input = f.read().split("\n")

rows = []

for input_str in input:
    rows.append(input_str.split(": ")[1])

copies = [1] * len(rows)
for i, row in enumerate(rows):
    multiplier = copies[i]
    winning_row, my_row = row.split(" | ")
    winning_nums = list(filter(None, winning_row.split(" ")))
    my_nums = list(filter(None, my_row.split(" ")))
    matches = 0
    for num in winning_nums:
        if num in my_nums:
            matches += 1
    for m in range(matches):
        if i + m + 1 < len(rows):
            copies[i + m + 1] += multiplier

print(sum(copies))

