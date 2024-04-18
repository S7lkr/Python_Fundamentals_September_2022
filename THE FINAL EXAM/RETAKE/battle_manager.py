players = {}

instructions = input()
while instructions != "Results":
    instructions = instructions.split(":")
    command = instructions[0]
    name = instructions[1]
    if command == "Add":
        hp = int(instructions[2])
        mana = int(instructions[3])
        if name not in players.keys():
            players[name] = [hp, mana]
        else:
            players[name][0] += hp
    elif command == "Attack":
        defender = instructions[2]
        damage = int(instructions[3])
        if name in players.keys() and defender in players.keys():
            players[defender][0] -= damage
            players[name][1] -= 1
            if players[defender][0] <= 0:
                del players[defender]
                print(f"{defender} was disqualified!")
            if players[name][1] <= 0:
                del players[name]
                print(f"{name} was disqualified!")
    elif command == "Delete":
        if name == "All":
            players.clear()
        if name in players.keys():
            del players[name]
    instructions = input()

print(f"People count: {len(players.keys())}")
[print(f"{player} - {stats[0]} - {stats[1]}") for player, stats in players.items()]