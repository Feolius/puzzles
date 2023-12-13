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

def calc_sums(puzzles, multiplier):
    res_sum = 0
    for puzzle in puzzles:
        reflection = None
        for i in range(len(puzzle) - 1):
            top_index = i
            bottom_index = i + 1
            while True:
                if top_index < 0:
                    reflection = i
                    break
                if bottom_index == len(puzzle):
                    reflection = i
                    break
                if puzzle[top_index] != puzzle[bottom_index]:
                    break
                top_index -= 1
                bottom_index += 1
        if reflection is not None:
            res_sum += (reflection + 1) * multiplier
    return res_sum


res = calc_sums(puzzles, 100) + calc_sums(puzzles_transp, 1)

print(res)