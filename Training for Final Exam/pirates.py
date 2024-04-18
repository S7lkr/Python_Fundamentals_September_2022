def plunder(a_town, the_people, kg_gold):
    pirate_diary[a_town][0] -= the_people
    pirate_diary[a_town][1] -= kg_gold
    print(f"{a_town} plundered! {gold} gold stolen, {people} citizens killed.")
    town_validator(a_town)
    return pirate_diary


def town_validator(a_town):
    if pirate_diary[a_town][0] <= 0 or pirate_diary[a_town][1] <= 0:
        del pirate_diary[a_town]
        print(f"{a_town} has been wiped off the map!")


def prosper(a_town, kg_gold):
    pirate_diary[a_town][1] += kg_gold
    return pirate_diary


info = input().split("||")
pirate_diary = {}

while info[0] != "Sail":
    city, population, gold = info[0], int(info[1]), int(info[2])
    if city not in pirate_diary.keys():
        pirate_diary[city] = [population, gold]
    else:
        pirate_diary[city][0] += population
        pirate_diary[city][1] += gold
    info = input().split("||")

instructions = input().split("=>")
while instructions[0] != "End":
    action = instructions[0]
    town = instructions[1]
    if action == "Plunder":
        people = int(instructions[2])
        gold = int(instructions[3])
        pirate_diary = plunder(town, people, gold)
    elif action == "Prosper":
        gold = int(instructions[2])
        if gold >= 0:
            pirate_diary = prosper(town, gold)
            print(f"{gold} gold added to the city treasury. {town} now has {pirate_diary[town][1]} gold.")
        else:
            print(f"Gold added cannot be a negative number!")
    instructions = input().split("=>")

if pirate_diary:
    print(f"Ahoy, Captain! There are {len(pirate_diary.keys())} wealthy settlements to go to:")
    for the_town, people_gold in pirate_diary.items():
        print(f"{the_town} -> Population: {people_gold[0]} citizens, Gold: {people_gold[1]} kg")
else:
    print("Ahoy, Captain! All targets have been plundered and destroyed!")