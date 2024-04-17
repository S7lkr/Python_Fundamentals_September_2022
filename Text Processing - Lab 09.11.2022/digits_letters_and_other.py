def is_character(symbol):
    if symbol.isalpha():
        return True
    return False


def is_digit(symbol):
    if symbol.isdigit():
        return True
    return False


text = input()
chars = ""
digits = ""
other_symbols = ""
for ch in text:
    if is_character(ch):
        chars += ch
    elif is_digit(ch):
        digits += ch
    else:
        other_symbols += ch

print(digits)
print(chars)
print(other_symbols)