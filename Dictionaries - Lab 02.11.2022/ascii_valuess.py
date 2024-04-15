letters = input().split(', ')

ascii_dict = {letter: ord(letter) for letter in letters}
# for letter in letters:
#     ascii_dict[letter] = ord(letter)

print(ascii_dict)