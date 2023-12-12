f = open("input.txt")

input = f.read().split("\n")

rows = []
for input_string in input:
    row, groups_string = input_string.split(" ")
    groups = list(map(lambda item: int(item), groups_string.split(",")))
    rows.append({
        "row": row,
        "groups": groups
    })


def count_arranges(row, groups):
    group_length = groups[0]
    most_right_start_index = len(row) - len(groups) - sum(groups) + 1
    row_sum = 0
    start_index = 0
    while start_index <= most_right_start_index:
        for i in range(group_length):
            if row[i + start_index] == ".":
                break
            elif row[i + start_index] == '#':
                most_right_start_index = min(most_right_start_index, i + start_index)
                continue
        else:
            if len(row) > start_index + group_length:
                if row[start_index + group_length] != "#":
                    if len(groups) > 1:
                        row_sum += count_arranges(row[start_index + group_length + 1:], groups[1:])
                    else:
                        if "#" not in row[start_index + group_length + 1:]:
                            row_sum += 1


            else:
                row_sum += 1
        start_index += 1
    return row_sum

res = 0
for row in rows:
    res += count_arranges(row["row"], row["groups"])



print(res)