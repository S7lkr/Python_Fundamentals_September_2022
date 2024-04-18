inventory = input().split(', ')
command = input()

while command != 'Craft!':
    command = command.split(' - ')
    if command[0] == 'Collect':
        item = command[1]
        if item not in inventory:
            inventory.append(item)
    elif command[0] == 'Drop':
        item = command[1]
        if item in inventory:
            inventory.remove(item)
    elif command[0] == 'Combine Items':
        old, new = command[1].split(':')
        if old in inventory:
            inventory.insert(inventory.index(old)+1, new)
    elif command[0] == 'Renew':
        item = command[1]
        if item in inventory:
            inventory.append(inventory.pop(inventory.index(item)))
    command = input()

print(', '.join(inventory))