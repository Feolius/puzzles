f = open("input.txt")

input = f.read().splitlines()

code_strings = []

data_started = False
data = []
for input_string in input:
    if not input_string:
        data_started = True
        continue
    if data_started:
        input_string = input_string.lstrip("{").rstrip("}")
        string_parts = input_string.split(",")
        item = {}
        for string_part in string_parts:
            prop, val = string_part.split("=")
            item[prop] = int(val)
        data.append(item)
    else:
        code_strings.append(input_string)

FUNC = "func"
CONDITION_CHAIN = "condition_chain"
DEFAULT_ACTION = "default_action"
CONDITION = "condition"
CONDITION_COMPARATOR = "condition_comparator"
CONDITION_ACTION = "condition_body"
COMPARATOR_PROP_OPERAND = "comparator_prod_operand"
COMPARATOR_NUMBER_OPERAND = "comparator_number_operand"
COMPARATOR_OPERATOR = "comparator_operator"
FUNC_CALL = "func_call"
RETURN = "return"


class Node:
    def __init__(self, type):
        self.type = type
        self.children = []


def build_ast(code_strings):
    ast = {}
    for code_string in code_strings:
        func_code_start_i = 0
        func_name = []
        for i, char in enumerate(code_string):
            if char == "{":
                func_code_start_i = i + 1
                break
            func_name.append(char)
        func_name = "".join(func_name)
        func_node = Node(FUNC)
        func_code_string = code_string[func_code_start_i:-1]
        func_code_parts = func_code_string.split(",")

        default_action_string = func_code_parts.pop()
        default_action_node = get_action_node(default_action_string)
        condition_chain_node = Node(CONDITION_CHAIN)
        for func_code_part in func_code_parts:
            condition_node = Node(CONDITION)

            condition_comparator_string, condition_action_string = func_code_part.split(":")
            condition_action_node = get_action_node(condition_action_string)

            comparator_node = Node(CONDITION_COMPARATOR)
            comparator_prop_operand_node = Node(COMPARATOR_PROP_OPERAND)
            comparator_prop_operand_node.children.append(condition_comparator_string[0])
            comparator_operator_node = Node(COMPARATOR_OPERATOR)
            comparator_operator_node.children.append(condition_comparator_string[1])
            comparator_number_operand_node = Node(COMPARATOR_NUMBER_OPERAND)
            comparator_number_operand_node.children.append(int(condition_comparator_string[2:]))
            comparator_node.children.extend(
                [comparator_prop_operand_node, comparator_operator_node, comparator_number_operand_node])
            condition_node.children.extend([comparator_node, condition_action_node])
            condition_chain_node.children.append(condition_node)
        func_node.children.extend([condition_chain_node, default_action_node])
        ast[func_name] = func_node
    return ast


def get_action_node(action_string):
    if action_string == "A" or action_string == "R":
        return_node = Node(RETURN)
        return_node.children.append(action_string)
        return return_node
    else:
        func_call_node = Node(FUNC_CALL)
        func_call_node.children.append(action_string)
        return func_call_node


ast = build_ast(code_strings)

def handle_action_node(item, node):
    if node.type == RETURN:
        return node.children[0] == "A"
    if node.type == FUNC_CALL:
        func_name = node.children[0]
        return handle_func_node(item, ast[func_name])
    raise Exception("Wrong action")


def handle_func_node(item, node):
    condition_chain_result = handle_condition_chain_node(item, node.children[0])
    if condition_chain_result is not None:
        return condition_chain_result
    return handle_action_node(item, node.children[1])


def handle_condition_chain_node(item, node):
    for condition_node in node.children:
        condition_result = handle_condition_node(item, condition_node)
        if condition_result is not None:
            return condition_result
    return None


def handle_condition_node(item, node):
    if handle_comparator_node(item, node.children[0]):
        return handle_action_node(item, node.children[1])
    else:
        return None


def handle_comparator_node(item, node):
    item_operand_value = item[node.children[0].children[0]]
    if node.children[1].children[0] == ">":
        return item_operand_value > node.children[2].children[0]
    else:
        return item_operand_value < node.children[2].children[0]


res = 0
for item in data:
    item_result = handle_func_node(item, ast["in"])
    if item_result:
        for prop in item:
            res += item[prop]





print(res)
