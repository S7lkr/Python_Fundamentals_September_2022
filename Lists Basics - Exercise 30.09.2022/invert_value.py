string = input().split(' ') # SPLIT the string by ' ' or TRANSFORM 'string' into a list, removing all the ' ' (spaces)
inverted = list()

for num in range(len(string)):
    if int(string[num]) < 0:
        inverted.append(abs(int(string[num])))
    else:
        inverted.append(int(string[num]) * -1)
print(inverted)