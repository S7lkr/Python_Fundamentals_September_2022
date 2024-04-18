def replaced(msg, old, new):
    msg = msg.replace(old, new)
    return msg


def remove(msg, sub_str):
    msg = msg.replace(sub_str, "")
    return msg


def includes_sub(msg, sub_str):
    if sub_str in msg:
        return f"True"
    return f"False"


def change(msg, low_or_up):
    if low_or_up == "Lower":
        msg = msg.lower()
    else:
        msg = msg.upper()
    return msg


def reverse_sub(msg, start, end):
    sub = ""
    if 0 <= start < end < len(msg):
        sub = msg[start:end + 1]
    return sub


text = input()
message = text

command = input()
while command != "Easter":
    command = command.split(" ")
    act = command[0]
    if act == "Replace":
        old_ch = command[1]
        new_ch = command[2]
        message = replaced(message, old_ch, new_ch)
        print(message)
    elif act == "Remove":
        substring = command[1]
        message = remove(message, substring)
        print(message)
    elif act == "Includes":
        string = command[1]
        print(includes_sub(message, string))
    elif act == "Change":
        low_up = command[1]
        message = change(message, low_up)
        print(message)
    elif act == "Reverse":
        start_ind = int(command[1])
        end_ind = int(command[2])
        substring = reverse_sub(message, start_ind, end_ind)
        print(substring[::-1])
    command = input()