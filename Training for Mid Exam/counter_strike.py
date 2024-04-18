total_energy = int(input())
distance = input()
battles_won = 0
energy_left = True

while distance != 'End of battle':
    if total_energy <= 0:
        energy_left = False
        break
    if battles_won % 3 == 0 and battles_won >= 1:
        total_energy += battles_won
    distance = int(distance)
    if total_energy < distance:
        energy_left = False
        break
    total_energy -= distance
    battles_won += 1
    distance = input()

if energy_left:
    print(f'Won battles: {battles_won}. Energy left: {total_energy}')
else:
    print(f"Not enough energy! Game ends with {battles_won} won battles and {total_energy} energy")