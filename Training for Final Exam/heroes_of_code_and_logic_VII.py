n = int(input())
heroes = {}

for hero in range(n):
    info = input().split(" ")
    hero_name, hp, mp = info[0], int(info[1]), int(info[2])
    if hero not in heroes.keys():
        heroes[hero_name] = []
    heroes[hero_name] = [hp, mp]

action = input().split(" - ")
while action[0] != "End":
    a_hero = action[1]
    if action[0] == "CastSpell":
        mp_needed = int(action[2])
        spell_name = action[3]
        if mp_needed <= heroes[a_hero][1]:
            heroes[a_hero][1] -= mp_needed
            print(f"{a_hero} has successfully cast {spell_name} and now has {heroes[a_hero][1]} MP!")
        else:
            print(f"{a_hero} does not have enough MP to cast {spell_name}!")
    elif action[0] == "TakeDamage":
        damage = int(action[2])
        attacker = action[3]
        if damage < heroes[a_hero][0]:
            heroes[a_hero][0] -= damage
            print(f"{a_hero} was hit for {damage} HP by {attacker} and now has {heroes[a_hero][0]} HP left!")
        else:
            del heroes[a_hero]
            print(f"{a_hero} has been killed by {attacker}!")
    elif action[0] == "Recharge":
        amount = int(action[2])
        before_recharge = heroes[a_hero][1]
        heroes[a_hero][1] += amount
        if heroes[a_hero][1] > 200:
            heroes[a_hero][1] = 200
        print(f"{a_hero} recharged for {heroes[a_hero][1] - before_recharge} MP!")
    elif action[0] == "Heal":
        hp_amount = int(action[2])
        before_heal = heroes[a_hero][0]
        heroes[a_hero][0] += hp_amount
        if heroes[a_hero][0] > 100:
            heroes[a_hero][0] = 100
        print(f"{a_hero} healed for {heroes[a_hero][0] - before_heal} HP!")
    action = input().split(" - ")

for hero, hp_mp in heroes.items():
    print(f"{hero}\n HP: {hp_mp[0]}\n MP: {hp_mp[1]}")
