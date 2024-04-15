def chars_between(start, end):
    for ch in range(ord(start)+1, ord(end)):
        print(chr(ch), end=' ')


start_char = input()
end_char = input()
chars_between(start_char, end_char)