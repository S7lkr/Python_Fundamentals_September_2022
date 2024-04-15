command = input()
small_commands = ('coding', 'cat', 'dog', 'movie')
upper_commands = ('CODING', 'CAT', 'DOG', 'MOVIE')
coffee_cnt = 0

while command != 'END':
    if coffee_cnt >= 5:
        print('You need extra sleep')
        break
    if command in small_commands:
        coffee_cnt += 1
    elif command in upper_commands:
        coffee_cnt += 2
    else:
        command = input()
        continue
    command = input()
else:
    print(coffee_cnt)