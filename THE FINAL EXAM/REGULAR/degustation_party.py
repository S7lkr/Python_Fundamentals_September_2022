testers = {}

unliked_cnt = 0

command = input()
while command != "Stop":
    action, guest, meal = command.split("-")
    if action == "Like":
        if guest not in testers.keys():
            testers[guest] = [meal]
        elif meal not in testers[guest]:
            testers[guest].append(meal)
    elif action == "Dislike":
        if guest in testers.keys():
            if meal in testers[guest]:
                print(f"{guest} doesn't like the {meal}.")
                testers[guest].remove(meal)
                unliked_cnt += 1
            else:
                print(f"{guest} doesn't have the {meal} in his/her collection.")
        else:
            print(f"{guest} is not at the party.")
    command = input()

for guest, meals in testers.items():
    print(f"{guest}: {', '.join(meals)}")
print(f"Unliked meals: {unliked_cnt}")