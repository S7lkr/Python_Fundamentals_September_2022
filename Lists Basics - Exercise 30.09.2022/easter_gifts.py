def out_of_stock(g):
    for ind in range(len(gifts)):
        if gift == gifts[ind]:
            gifts[ind] = 'None'
    return gifts


def required(g, i):
    if 0 <= index < len(gifts) - 1:
        gifts[index] = gift
    return gifts


def just_in_case(g):
    gifts[-1] = g
    return gifts


gifts = input().split(" ")
command = input()
while command != 'No Money':
    command = command.split(" ")
    gift = command[1]
    if command[0] == 'OutOfStock':
        gifts = out_of_stock(gift)
    elif command[0] == 'Required':
        gift = command[1]
        index = int(command[2])
        gifts = required(gift, index)
    elif command[0] == 'JustInCase':
        just_in_case(gift)
    command = input()

while "None" in gifts:
    gifts.remove("None")
print(' '.join(gifts))