def take_odd(text):
    text2 = ""
    for k in range(len(text)):
        if k % 2 != 0:
            text2 += text[k]
    return text2


def cut(text, ind, leng):
    text = text[:ind] + text[ind + leng::]
    return text


def substitution(text, sub_str, subst):
    text = text.replace(sub_str, subst)
    return text


string = input()
command = input().split(" ")
while command[0] != "Done":
    if command[0] == "TakeOdd":
        string = take_odd(string)
        print(string)
    elif command[0] == "Cut":
        index = int(command[1])
        length = int(command[2])
        string = cut(string, index, length)
        print(string)
    elif command[0] == "Substitute":
        substring = command[1]
        substitute = command[2]
        if substring in string:
            string = substitution(string, substring, substitute)
            print(string)
        else:
            print("Nothing to replace!")
    command = input().split(" ")

print(f"Your password is: {string}")