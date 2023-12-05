f = open("input.txt")

input = f.read().split("\n")


# I_MAX = 10
# J_MAX = 10
I_MAX = 139
J_MAX = 139

matrix = []
for stringRow in input:
    row = []
    for char in stringRow:
        if char != "." and not char.isdigit():
            row.append("$")
        else:
            row.append(char)
    matrix.append(row)


def checkLocality(i, jStart, jEnd):
    jStartRowCheck = jStart - 1
    jEndRowCheck = jEnd + 1
    if jStart == 0:
        jStartRowCheck = 0
        leftSideCheck = False
    else:
        leftSideCheck = matrix[i][jStartRowCheck] == "$"
    if jEnd == J_MAX:
        jEndRowCheck = J_MAX
        rightSideCheck = False
    else:
        if jEndRowCheck > J_MAX:
            print(i, jEndRowCheck)
        rightSideCheck = matrix[i][jEndRowCheck] == "$"
    if leftSideCheck or rightSideCheck:
        return True
    if i == 0:
        return checkSymbolInRowPart(i + 1, jStartRowCheck, jEndRowCheck)
    elif i == I_MAX:
        return checkSymbolInRowPart(i - 1, jStartRowCheck, jEndRowCheck)
    else:
        return checkSymbolInRowPart(i - 1, jStartRowCheck, jEndRowCheck) or checkSymbolInRowPart(i + 1, jStartRowCheck,
                                                                                                 jEndRowCheck)


def checkSymbolInRowPart(i, jStart, jEnd):
    for char in matrix[i][jStart:jEnd + 1]:
        if char == "$":
            return True
    return False


res = 0
for i, row in enumerate(matrix):
    jNumberStart = None
    for j, char in enumerate(row):
        if char.isdigit():
            if jNumberStart is None:
                jNumberStart = j
            if j == J_MAX and checkLocality(i, jNumberStart, j):
                number = int("".join(matrix[i][jNumberStart:j + 1]))
                res += number
        elif jNumberStart is not None:
            if checkLocality(i, jNumberStart, j - 1):
                number = int("".join(matrix[i][jNumberStart:j]))
                res += number
            jNumberStart = None

print(res)
