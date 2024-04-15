circle = input().split()
kill_order = int(input())
executed = []
cnt = 0     # we will count every soldier: 1, 2, 3
index = 0   # this will be the index representing the soldier

while len(circle) > 0:      # while there are still soldiers in the 'circle':
    cnt += 1        # we start from 1st soldier and:
    if cnt % kill_order == 0:   # check if he is the 'kill_order', so he should be executed: 3 % 3 != 0, 6 % 3 != 0...
        executed.append(circle.pop(index))      # add to the 'executed' list the removed from 'circle' list soldier
    else:       # if the soldier is not the one should be killed:
        index += 1      # then index will increase by 1
    if index >= len(circle):    # when the index is bigger than 'circle', we start from beginning: index = 0
        index = 0

print(str(executed).replace(' ', '').replace('\'', '')) # this makes a string list into a int list