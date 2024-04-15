materials = input().split(" ")
inventory = {"shards": 0, "fragments": 0, "motes": 0}
legendary_item = {"shards": "Shadowmourne", "fragments": "Valanyr", "motes": "Dragonwrath"}
item_obtained = False

while not item_obtained:
    for index in range(0, len(materials), 2):
        quantity = materials[index]
        element = materials[index + 1].lower()
        if element not in inventory.keys():
            inventory[element] = 0
        inventory[element] += int(quantity)
        if element in legendary_item.keys() and inventory[element] >= 250:
            print(f"{legendary_item[element]} obtained!")
            inventory[element] -= 250
            item_obtained = True
            break
    if item_obtained:
        break
    materials = input().split(" ")

for key, value in inventory.items():
    print(f"{key}: {value}")