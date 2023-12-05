f = open("input.txt")

input = f.read().split("\n")


# I_MAX = 10
# J_MAX = 10
I_MAX = 140
J_MAX = 140

matrix = []
for stringRow in input:
    row = ["."]
    for char in stringRow:
        if char == "*" or char.isdigit():
            row.append(char)
        else:
            row.append(".")
    row.append(".")
    matrix.append(row)


def locality_numbers_extractor(i, j):
    res = []
    upper_numbers = middle_index_row_numbers_extractor(i - 1, j)
    if matrix[i][j - 1].isdigit():
        number_left_j = walk_number_left(i, j - 1)
        res.append(get_number(i, number_left_j, j - 1))
    if matrix[i][j + 1].isdigit():
        number_right_j = walk_number_right(i, j + 1)
        res.append(get_number(i, j + 1, number_right_j))
    lower_numbers = middle_index_row_numbers_extractor(i + 1, j)

    return res + upper_numbers + lower_numbers


def middle_index_row_numbers_extractor(i, j):
    res = []
    number_left_j = number_right_j = None
    if matrix[i][j].isdigit():
        number_left_j = walk_number_left(i, j)
        number_right_j = walk_number_right(i, j)
        res.append(get_number(i, number_left_j, number_right_j))

    left_checked = False
    if number_left_j is not None and number_left_j < j:
        left_checked = True

    right_checked = False
    if number_right_j is not None and number_right_j > j:
        right_checked = True

    if not left_checked and matrix[i][j - 1].isdigit():
        number_left_j = walk_number_left(i, j - 1)
        res.append(get_number(i, number_left_j, j - 1))
    if not right_checked and matrix[i][j + 1].isdigit():
        number_right_j = walk_number_right(i, j + 1)
        res.append(get_number(i, j + 1, number_right_j))

    return res


def walk_number_left(i, j):
    left_j = j
    while matrix[i][left_j - 1].isdigit():
        left_j -= 1
    return left_j


def walk_number_right(i, j):
    right_j = j
    while matrix[i][right_j + 1].isdigit():
        right_j += 1
    return right_j


def get_number(i, j_start, j_end):
    return int("".join(matrix[i][j_start:j_end + 1]))


res = 0
for i, row in enumerate(matrix):
    for j, char in enumerate(row):
        if char == "*":
            numbers = locality_numbers_extractor(i, j)
            if len(numbers) == 2:
                res += numbers[0] * numbers[1]

print(res)
