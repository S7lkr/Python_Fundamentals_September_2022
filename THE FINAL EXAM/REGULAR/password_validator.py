def make_upper(ind, passw):
    passw = passw.replace(passw[ind], passw[ind].upper(), 1)
    return passw


def make_lower(ind, passw):
    passw = passw.replace(passw[ind], passw[ind].lower(), 1)
    return passw


def insert(ind, ch, passw):
    if ind < len(passw):
        passw = passw[:ind] + ch + passw[ind:]
    return passw


def replace_all(ch, val, passw):
    if ch in passw:
        number = ord(ch)
        number += val
        number = chr(number)
        passw = passw.replace(ch, number)
    return passw


def length(passw):
    if len(passw) >= 8:
        return True
    return False


def letters_only(passw):
    for ch in passw:
        if ch.isalnum() or ch == "_":
            continue
        else:
            return False


def upper_check(passw):
    for ch in passw:
        if ch.isupper():
            return True
    return False


def lower_check(passw):
    for ch in passw:
        if ch.islower():
            return True
    return False


def has_digit(passw):
    for ch in passw:
        if ch.isdigit():
            return True
    return False


def password_validator(passw):
    if not length(password):
        print(f"Password must be at least 8 characters long!")
    if not letters_only(password):
        print(f"Password must consist only of letters, digits and _!")
    if not upper_check(password):
        print(f"Password must consist at least one uppercase letter!")
    if not lower_check(password):
        print(f"Password must consist at least one lowercase letter!")
    if not has_digit(password):
        print(f"Password must consist at least one digit!")
    return True


raw_password = input()
password = raw_password

command = input()
while command != "Complete":
    command = command.split(" ")
    act = command[0]
    if act == "Make":
        up_low = command[1]
        index = int(command[2])
        if up_low == "Upper":
            password = make_upper(index, password)
        elif up_low == "Lower":
            password = make_lower(index, password)
        print(password)
    elif act == "Insert":
        index = int(command[1])
        char = command[2]
        password = insert(index, char, password)
        print(password)
    elif act == "Replace":
        char = command[1]
        value = int(command[2])
        password = replace_all(char, value, password)
        print(password)
    elif act == "Validation":
        password_validator(password)
    command = input()