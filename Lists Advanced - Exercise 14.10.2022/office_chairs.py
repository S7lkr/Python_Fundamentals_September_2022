rooms = int(input())
free_chairs_left = 0

for room in range(1, rooms + 1):
    chairs_and_visitors = input().split()
    chairs = len(chairs_and_visitors[0])
    visitors = int(chairs_and_visitors[1])

    if chairs >= visitors:
        chairs_left_in_room = chairs - visitors
        free_chairs_left += chairs_left_in_room
    else:
        chairs_needed = visitors - chairs
        free_chairs_left -= chairs_needed
        print(f"{chairs_needed} more chairs needed in room {room}")

if free_chairs_left >= 0:
    print(f"Game On, {free_chairs_left} free chairs left")