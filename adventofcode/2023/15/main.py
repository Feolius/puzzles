f = open("input.txt")

commands = f.read().split(",")


def calc_hash(code):
    current_value = 0
    for char in code:
        current_value += ord(char)
        current_value = current_value * 17
        current_value = current_value & 255
    return current_value


res = 0
for command in commands:
    res += calc_hash(command)

print(res)