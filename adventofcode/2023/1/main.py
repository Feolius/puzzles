f = open("input.txt")

input = f.read().split("\n")
spelledDigits = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
numbers = []

for string in input:
    startDigitPos = None
    endDigitPos = None
    for charPos in range(len(string)):
        if string[charPos].isdigit():
            if startDigitPos is None:
                startDigitPos = charPos
            else:
                endDigitPos = charPos
    if endDigitPos is None:
        endDigitPos = startDigitPos
    mostLeftSpelledDigitPos = None
    mostRightSpelledDigitPos = None
    mostLeftSpelledDigit = None
    mostRightSpelledDigit = None
    for i, spelledDigit in enumerate(spelledDigits):
        lindex = string.find(spelledDigit)
        if lindex == -1:
            continue
        rindex = string.rfind(spelledDigit)
        if mostLeftSpelledDigit is None or mostLeftSpelledDigitPos > lindex:
            mostLeftSpelledDigitPos = lindex
            mostLeftSpelledDigit = i + 1
        if mostRightSpelledDigit is None or mostRightSpelledDigitPos < rindex:
            mostRightSpelledDigitPos = rindex
            mostRightSpelledDigit = i + 1
    if startDigitPos is not None:
        leftDigitChar = string[startDigitPos]
    if startDigitPos is None or (mostLeftSpelledDigitPos is not None and mostLeftSpelledDigitPos < startDigitPos):
        leftDigitChar = str(mostLeftSpelledDigit)

    if endDigitPos is not None:
        rightDigitChar = string[endDigitPos]

    if endDigitPos is None or (mostRightSpelledDigitPos is not None and mostRightSpelledDigitPos > endDigitPos):
        rightDigitChar = str(mostRightSpelledDigit)
    number = int(leftDigitChar + rightDigitChar)
    numbers.append(number)


res = sum(numbers)
print(res)
