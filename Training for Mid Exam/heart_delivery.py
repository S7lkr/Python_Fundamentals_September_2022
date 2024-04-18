neighborhood = list(map(int, input().split('@')))
command = input()
last_jump = 0
cupid_last_position = 0
houses_failed = 0
mission_success = True

while command != 'Love!':
    command = command.split()
    jump = int(command[1])
    jump += last_jump
    cupid_last_position = jump
    if jump >= len(neighborhood):
        jump = 0
    if neighborhood[jump] == 0:
        print(f"Place {jump} already had Valentine's day.")
        command = input()
        continue
    neighborhood[jump] -= 2
    if neighborhood[jump] == 0:
        print(f"Place {jump} has Valentine's day.")
    last_jump = jump
    command = input()

print(f"Cupid's last position was {cupid_last_position}.")

for house in neighborhood:
    if house != 0:
        houses_failed += 1

if houses_failed > 0:
    mission_success = False

if mission_success:
    print(f"Mission was successful.")
else:
    print(f"Cupid has failed {houses_failed} places.")


# lst = ['a', 'b', 'b', 'c', 'd']
# jump = int(input())
# last_jump = 0
#
# while jump != 'end':
#     jump += last_jump
#     if jump >= len(lst):
#         jump -= len(lst)
#     print(lst[jump])
#     last_jump = jump
#     jump = int(input())
