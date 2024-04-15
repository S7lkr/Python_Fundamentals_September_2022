number_of_wagons = int(input())
command = input().split()
wagons = [0 for num in range(number_of_wagons)]

while command[0] != 'End':
    index = int(command[1])
    if command[0] == 'add':
        wagons[number_of_wagons - 1] += index
    elif command[0] == 'insert':
        people = int(command[2])
        wagons[index] += int(people)
    elif command[0] == 'leave':
        people = int(command[2])
        wagons[index] -= people
    command = input().split()
print(wagons)