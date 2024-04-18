days = int(input())
players = int(input())
energy = float(input())
water_day_for_person = float(input())
food_day_for_person = float(input())
energy_left = True
total_food = players * food_day_for_person * days
total_water = players * water_day_for_person * days

for day in range(1, days + 1):
    energy_loss = float(input())
    energy -= energy_loss
    if energy <= 0:
        energy_left = False
        break
    if day % 2 == 0:
        energy += 0.05 * energy
        total_water -= total_water * 0.3
    if day % 3 == 0:
        total_food -= total_food / players
        energy += energy * 0.1

if energy_left:
    print(f'You are ready for the quest. You will be left with - {energy:.2f} energy!')
    # print(f'{total_food:.2f}')
    # print(f'{total_water:.2f}')
else:
    print(f'You will run out of energy. You will be left with {total_food:.2f} food '
          f'and {total_water:.2f} water.')