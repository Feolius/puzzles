f = open("input.txt")

input = f.read().split("\n")

RED_MAX = 12
GREEN_MAX = 13
BLUE_MAX = 14
COLOUR_TO_MAX = {
    "red": RED_MAX,
    "green": GREEN_MAX,
    "blue": BLUE_MAX
}

resSum = 0
for i, string in enumerate(input):
    requirements = {
        "red": None,
        "green": None,
        "blue": None
    }
    game = string.split(": ")[1]
    sets = game.split("; ")
    for set in sets:
        rolls = set.split(", ")
        for roll in rolls:
            num, colour = roll.split(" ")
            if requirements[colour] is None or int(num) > requirements[colour]:
                requirements[colour] = int(num)
    resSum += requirements["red"]*requirements["green"]*requirements["blue"]


print(resSum)