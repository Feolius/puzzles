f = open("input.txt")

command_strings = f.read().split(",")
commands = []
for command_string in command_strings:
    if "=" in command_string:
        code, focal_length = command_string.split("=")
        commands.append({
            "code": code,
            "fl": int(focal_length)
        })
    else:
        commands.append({
            "code": command_string[:-1],
            "fl": "-"
        })


def calc_hash(code):
    current_value = 0
    for char in code:
        current_value += ord(char)
        current_value = current_value * 17
        current_value = current_value & 255
    return current_value


boxes = [{"next_index": 0, "lenses": {}} for _ in range(256)]
for command in commands:
    box_index = calc_hash(command["code"])
    if command["fl"] == "-":
        if command["code"] in boxes[box_index]["lenses"]:
            lense_index = boxes[box_index]["lenses"][command["code"]]["index"]
            del boxes[box_index]["lenses"][command["code"]]
            for code in boxes[box_index]["lenses"]:
                if boxes[box_index]["lenses"][code]["index"] > lense_index:
                    boxes[box_index]["lenses"][code]["index"] -= 1
            boxes[box_index]["next_index"] -= 1
    else:
        if command["code"] in boxes[box_index]["lenses"]:
            boxes[box_index]["lenses"][command["code"]] = {
                "fl": command["fl"],
                "index": boxes[box_index]["lenses"][command["code"]]["index"]
            }
        else:
            boxes[box_index]["lenses"][command["code"]] = {
                "fl": command["fl"],
                "index": boxes[box_index]["next_index"]
            }
            boxes[box_index]["next_index"] += 1


res = 0
for i, box in enumerate(boxes):
    for label, lense in box["lenses"].items():
        res += (i + 1)*(lense["index"] + 1)*lense["fl"]


print (res)
