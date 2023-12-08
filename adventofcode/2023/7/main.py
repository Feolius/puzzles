from functools import cmp_to_key

f = open("input.txt")

input = f.read().split("\n")

TOKEN_WEIGHTS = {
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "T": 10,
    "J": 11,
    "Q": 12,
    "K": 13,
    "A": 14
}

hands_processed = []
for string in input:
    input_hand, bid = string.split(" ")
    bid = int(bid)
    card_tokens = []
    for char in input_hand:
        card_tokens.append(TOKEN_WEIGHTS[char])
    tokens_frequencies = {}
    for token in card_tokens:
        if token not in tokens_frequencies:
            tokens_frequencies[token] = 1
        else:
            tokens_frequencies[token] += 1
    token_frequencies_values = tokens_frequencies.values()
    if 5 in token_frequencies_values:
        weight = 7
    elif 4 in token_frequencies_values:
        weight = 6
    elif 3 in token_frequencies_values and 2 in token_frequencies_values:
        weight = 5
    elif 3 in token_frequencies_values:
        weight = 4
    elif len([i for i,x in enumerate(token_frequencies_values) if x==2]) == 2:
        weight = 3
    elif 2 in token_frequencies_values:
        weight = 2
    else:
        weight = 1

    hand = {
        "cards": card_tokens,
        "weight": weight,
        "bid": bid
    }
    hands_processed.append(hand)

def hands_compare(h1, h2):
    if h1["weight"] < h2["weight"]:
        return -1
    elif h1["weight"] > h2["weight"]:
        return 1
    else:
        for i in range(5):
            if h1["cards"][i] < h2["cards"][i]:
                return -1
            elif h1["cards"][i] > h2["cards"][i]:
                return 1
            else:
                continue


hands_sorted = sorted(hands_processed, key=cmp_to_key(hands_compare))

res = 0
for i, hand in enumerate(hands_sorted):
    res += (i + 1)*hand["bid"]

print(res)



