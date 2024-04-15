quantity = int(input())
days_until_christmas = int(input())

ornament_set = 2
tree_skirt = 5
tree_garland = 3
tree_lights = 15

spirit_gained = 0
all_costs = 0

for day in range(1, days_until_christmas + 1):
    if day % 11 == 0:
        quantity += 2
    if day % 2 == 0:
        all_costs += ornament_set * quantity
        spirit_gained += 5
    if day % 3 == 0:
        all_costs += (tree_skirt + tree_garland) * quantity
        spirit_gained += 13
    if day % 5 == 0:
        all_costs += tree_lights * quantity
        spirit_gained += 17
        if day % 3 == 0:
            spirit_gained += 30
    if day % 10 == 0:
        spirit_gained -= 20
        all_costs += tree_skirt + tree_garland + tree_lights

if days_until_christmas % 10 == 0:
    spirit_gained -= 30

print(f"Total cost: {round(all_costs)}")
print(f"Total spirit: {spirit_gained}")