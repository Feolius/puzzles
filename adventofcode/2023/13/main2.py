f = open("input.txt")

input = f.read().split("\n")

puzzles = []
puzzle = []
puzzles_transp = []
puzzle_transp = ["" for _ in range(len(input[0]))]
for i, input_str in enumerate(input):
    if input_str == "":
        puzzles.append(puzzle)
        puzzles_transp.append(puzzle_transp)
        puzzle_transp = ["" for _ in range(len(input[i + 1]))]
        puzzle = []
        continue
    for j, char in enumerate(input_str):
        puzzle_transp[j] += char
    puzzle.append(input_str)
puzzles.append(puzzle)
puzzles_transp.append(puzzle_transp)

smudges = [None for _ in range(len(puzzles))]
def calc_sums(puzzles, multiplier):
    res_sum = 0
    for p, puzzle in enumerate(puzzles):
        reflection = None
        for i in range(len(puzzle) - 1):
            smudge = None
            top_index = i
            bottom_index = i + 1
            while True:
                if top_index < 0:
                    if smudge is not None:
                        reflection = i
                    break
                if bottom_index == len(puzzle):
                    if smudge is not None:
                        reflection = i
                    break
                if puzzle[top_index] != puzzle[bottom_index]:
                    if smudge is None:
                        smudge = get_smudge_index(puzzle[top_index], puzzle[bottom_index])
                        if smudge is not None:
                            top_index -= 1
                            bottom_index += 1
                            continue
                    break
                top_index -= 1
                bottom_index += 1
        if reflection is not None:
            res_sum += (reflection + 1) * multiplier
    return res_sum


def get_smudge_index(str1, str2):
    diff_index = None
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            if diff_index is not None:
                return None
            diff_index = i
    return diff_index




res = calc_sums(puzzles, 100) + calc_sums(puzzles_transp, 1)

print(res)