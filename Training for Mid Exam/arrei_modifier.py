numbers = list(map(int, input().split()))

while True:
    command = input()
    if command == 'end':
        break
    if command == 'decrease':
        numbers = [int(element) - 1 for element in numbers]
        continue
    command = command.split()
    num1 = int(command[1])
    num2 = int(command[2])
    if command[0] == 'swap':
        numbers[num1], numbers[num2] = numbers[num2], numbers[num1]
    elif command[0] == 'multiply':
        numbers[num1] *= numbers[num2]

print(', '.join(list(map(str, numbers))))