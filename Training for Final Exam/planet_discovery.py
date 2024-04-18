import re

n = int(input())
plant_rarity = {}
plant_ratings = {}

for pl in range(n):
    plant, rarity = input().split("<->")
    if plant not in plant_ratings.keys():
        plant_rarity[plant] = 0
        plant_ratings[plant] = []
    plant_rarity[plant] = int(rarity)

command = re.split(": | - ", input())
while command[0] != "Exhibition":
    plant = command[1]
    if command[0] == "Rate":
        rating = int(command[2])
        if plant in plant_ratings.keys():
            plant_ratings[plant].append(rating)
        else:
            print("error")
    elif command[0] == "Update":
        new_rarity = int(command[2])
        if plant in plant_rarity.keys():
            plant_rarity[plant] = new_rarity
        else:
            print("error")
    elif command[0] == "Reset":
        if plant in plant_ratings.keys():
            plant_ratings[plant] = []
        else:
            print("error")
    command = re.split(": | - ", input())

print(f"Plants for the exhibition:")
for key, value in plant_ratings.items():
    if value:
        average = sum(value) / len(value)
    else:
        average = 0
    print(f"- {key}; Rarity: {plant_rarity[key]}; Rating: {average:.2f}")