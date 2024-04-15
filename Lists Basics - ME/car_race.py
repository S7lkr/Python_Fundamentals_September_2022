time_table = input().split()
left_racer = time_table[0:len(time_table) // 2]
time_table.reverse()
right_racer = time_table[0:len(time_table) // 2]

left_time = 0
right_time = 0

for time in left_racer:
    if int(time) == 0:
        left_time *= 0.8
    left_time += int(time)

for time in right_racer:
    if int(time) == 0:
        right_time *= 0.8
    right_time += int(time)

if left_time < right_time:
    print(f"The winner is left with total time: {left_time:.1f}")
else:
    print(f"The winner is right with total time: {right_time:.1f}")