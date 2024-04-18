def insert_space(ind, msg):
    msg = msg[:ind] + " " + msg[ind:]
    return msg


def reverse(sub_str, msg):
    msg = msg.replace(sub_str, '', 1)
    msg += sub_str[::-1]
    return msg


def change_all(sub_str, repl, msg):
        msg = msg.replace(sub_str, repl)
        return msg


message = input()
command = input().split(":|:")
while command[0] != "Reveal":
    if command[0] == "InsertSpace":
        index = int(command[1])
        message = insert_space(index, message)
        print(message)
    elif command[0] == "Reverse":
        substring = command[1]
        if substring in message:
            message = reverse(substring, message)
            print(message)
        else:
            print("error")
    elif command[0] == "ChangeAll":
        substring = command[1]
        replacement = command[2]
        message = change_all(substring, replacement, message)
        print(message)
    command = input().split(":|:")
print(f"You have a new text message: {message}")