coffees = input().split()
number_of_commands = int(input())

for cmd in range(number_of_commands):
    command = input()
    if command == 'Reverse':
        coffees.reverse()
        continue
    command = command.split()
    if command[0] == 'Include':
        coffees.append(command[1])
    elif command[0] == 'Remove':
        first_last = command[1]
        amount = int(command[2])
        if amount < len(coffees):
            if first_last == 'first':
                coffees = [coffees[i] for i in range(len(coffees)) if i >= amount]
            elif first_last == 'last':
                coffees = [coffees[i] for i in range(len(coffees) - amount)]
    elif command[0] == 'Prefer':
        old = int(command[1])
        new = int(command[2])
        if 0 <= old < len(coffees) and 0 <= new < len(coffees):
            coffees[old], coffees[new] = coffees[new], coffees[old]

coffees = ' '.join(coffees)
print(f'Coffees:\n{coffees}')
