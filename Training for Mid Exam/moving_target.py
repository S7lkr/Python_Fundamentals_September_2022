def shoot(index, power, targets):
    if 0 <= index < len(targets):
        if power >= targets[index] or targets[index] <= 0:
            targets.pop(index)
        else:
            targets[index] -= power
    return targets


def add(index, value, targets):
    if 0 <= index < len(targets):
        targets.insert(index, value)
    else:
        print('Invalid placement!')
    return targets


def strike(index, radius, targets):
    validator_index = index - radius >= 0 and index + radius < len(targets)
    if validator_index:
        start_target_index = index - radius
        end_target_index = index + radius
        targets = [targets[i] for i in range(len(targets)) if i < start_target_index or i > end_target_index]
    else:
        print('Strike missed!')
    return targets


def moving_targets(targets):
    while True:
        command = input()
        if command == 'End':
            break
        command, index, value = command.split()
        index = int(index)
        value = int(value)
        if command == 'Shoot':
            targets = shoot(index, value, targets)
        elif command == 'Add':
            targets = add(index, value, targets)
        elif command == 'Strike':
            targets = strike(index, value, targets)

    result = '|'.join(list(map(str, targets)))
    print(result)


numbers = list(map(int, input().split()))
moving_targets(numbers)

# start = 1
# end = 3
# lst = [1, 2, 3, 4, 5]
# lst = [lst[i] for i in range(len(lst)) if i < start or i > end]
# print(lst)