f = open("input.txt")

input = f.read().split("\n")

sequences = []
for string in input:
    sequences.append(list(map(lambda item: int(item), string.split(" "))))


def get_prediction(sequence):
    if len(sequence) == 1:
        return sequence[0]


    next_sequence = []
    prev_item = sequence[0]
    all_equals = True
    for i in range(1, len(sequence)):
        if prev_item != sequence[i]:
            all_equals = False
        prev_item = sequence[i]
        next_sequence.append(sequence[i] - sequence[i - 1])

    if all_equals:
        return prev_item
    next_prediction = get_prediction(next_sequence)
    return next_prediction + sequence[len(sequence) - 1]


def get_backward_prediction(sequence):
    if len(sequence) == 1:
        return sequence[0]


    next_sequence = []
    prev_item = sequence[0]
    all_equals = True
    for i in range(1, len(sequence)):
        if prev_item != sequence[i]:
            all_equals = False
        prev_item = sequence[i]
        next_sequence.append(sequence[i] - sequence[i - 1])

    if all_equals:
        return prev_item
    next_prediction = get_backward_prediction(next_sequence)
    return sequence[0] - next_prediction


res = []
backward_res = []
for sequence in sequences:
    res.append(get_prediction(sequence))
    backward_res.append(get_backward_prediction(sequence))


print(sum(res))
print(sum(backward_res))