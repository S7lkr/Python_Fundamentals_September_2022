sequence = input().split()
move_cnt = 0
game_won = False

while True:
    command = input()
    if len(sequence) == 0:
        game_won = True
        break
    if command == 'end':
        break
    command = command.split()
    num1 = int(command[0])
    num2 = int(command[1])
    move_cnt += 1
    if num1 >= len(sequence) or num2 >= len(sequence) or num1 < 0 or num2 < 0 or num1 == num2:
        for index in command:
            sequence.insert(len(sequence)//2, '-' + str(move_cnt) + 'a')
        print('Invalid input! Adding additional elements to the board')
    elif sequence[num1] == sequence[num2]:
        element = sequence[num1]
        sequence = [num for num in sequence if num != element]
        print(f"Congrats! You have found matching elements - {element}!")
    else:
        print('Try again!')

if game_won:
    print(f"You have won in {move_cnt} turns!")
else:
    print(f"Sorry you lose :(\n{' '.join(sequence)}")