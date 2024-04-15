numbered_list = []  # create an empty list []

while True:
    command = input()   # input a string
    if command == 'End':    # compare
        break
    command = command.split('-')    # we make every command into a list with 2 elements: [number, action]
    priority = int(command[0])  # index 0 from the command will be 'priority'
    action = command[1]     # index 1 -> action
    numbered_list.append([priority, action])    # we make a nested list: [[2, 'walk'], [5, 'work']...]
                                            # the point is to make it SORTABLE by number
to_do_list = [action[1] for action in sorted(numbered_list)]    # we take only the 1st indexes from every list
print(to_do_list)                           # only the actions, and print ['coffee', 'dog', 'work', 'dinner']