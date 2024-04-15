def fire_extinguish(f_strength, water_quantity):
    if water_quantity >= f_strength:
        water_quantity -= f_strength
        cells.append(f_strength)
        print(f' - {f_strength}')
    return water_quantity


def water_validator():
    if water_quantity <= 0:
        return False
    return True


fires = input().split('#')
water_quantity = int(input())
cells = list()
effort = 0
water_left = True
print('Cells:')

for fire in fires:
    if not water_left:
        break
    fire_type, value = fire.split(' = ')
    value = int(value)
    if fire_type == 'High' and 81 <= value <= 125:
        water_quantity = fire_extinguish(value, water_quantity)
    elif fire_type == 'Medium' and 51 <= value <= 80:
        water_quantity = fire_extinguish(value, water_quantity)
    elif fire_type == 'Low' and 1 <= value <= 50:
        water_quantity = fire_extinguish(value, water_quantity)
    water_left = water_validator()

effort = sum(cells) * 0.25
print(f'Effort: {effort:.2f}')
print(f'Total Fire: {sum(cells)}')