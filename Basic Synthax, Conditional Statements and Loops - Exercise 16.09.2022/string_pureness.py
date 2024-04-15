n = int(input())

for _ in range(n):
    string = input()
    if ',' in string or '.' in string or '_' in string:
        print(f'{string} is not pure!')
    else:
        print(f'{string} is pure.')


# -- Method for finding a SYMBOL in text --
# letter = 't' # be aware for the CASE sensitiveness! 'T' is different from 't'
# name = 'Peter'
# print(letter in name) # either TRUE or FALSE; In that case it shall be TRUE


# -- Print all the characters in text --
# name = 'Jackson'
# for letter in name:
#     print(letter, end='')
#     print()