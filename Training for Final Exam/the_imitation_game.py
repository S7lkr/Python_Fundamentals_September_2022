def move(num, msg):
    cut_part = msg[:num]
    msg = msg[num:] + cut_part
    return msg


def insert(ind, val, msg):
    msg = msg[:ind] + val + msg[ind:]
    return msg


def change_all(sub_str, repl, msg):
    msg = msg.replace(sub_str, repl)
    return msg


message = input()
command = input().split("|")
while command[0] != "Decode":
    action = command[0]
    if action == "Move":
        letter_num = int(command[1])
        message = move(letter_num, message)
    elif action == "Insert":
        index = int(command[1])
        value = command[2]
        message = insert(index, value, message)
    elif action == "ChangeAll":
        substring = command[1]
        replaced = command[2]
        message = change_all(substring, replaced, message)
    command = input().split("|")
print(f"The decrypted message is: {message}")