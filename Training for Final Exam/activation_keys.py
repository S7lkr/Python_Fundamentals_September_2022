def contains(activ_key, sub_str):
    if sub_str in activ_key:
        return f"{activ_key} contains {sub_str}"
    else:
        return "Substring not found!"


def flip(activ_key, up_low, start, end):
    sliced_part = activ_key[start:end]
    if up_low == "Upper":
        sliced_part = sliced_part.upper()
    else:
        sliced_part = sliced_part.lower()
    activ_key = activ_key[0:start] + sliced_part + activ_key[end:]
    return activ_key


def slice_str(activ_key, start, end):
    activ_key = activ_key[:start] + activ_key[end:]
    return activ_key


raw_key = input()
activation_key = raw_key

while True:
    instructions = input()
    if instructions == "Generate":
        break
    instructions = instructions.split(">>>")
    act = instructions[0]
    if act == "Contains":
        substring = instructions[1]
        print(contains(activation_key, substring))
    elif act == "Flip":
        upper_lower = instructions[1]
        start_index = int(instructions[2])
        end_index = int(instructions[3])
        activation_key = flip(activation_key, upper_lower, start_index, end_index)
        print(activation_key)
    elif act == "Slice":
        start_index = int(instructions[1])
        end_index = int(instructions[2])
        activation_key = slice_str(activation_key, start_index, end_index)
        print(activation_key)
print(f"Your activation key is: {activation_key}")