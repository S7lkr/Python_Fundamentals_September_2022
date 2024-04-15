star_wars = {}

while True:
    current_member = input()
    if current_member == 'Lumpawaroo':
        break
    member_NOT_in_star_wars = True     # NOTE: this will keep an eye for if member EXISTS ANYWHERE in the dictionary
    if " | " in current_member:
        force, member = current_member.split(" | ")
        for value in star_wars.values():    # first we check if member is in ANY value
            if member in value:     # if he is ANYWHERE in dict (no matter which key),
                member_NOT_in_star_wars = False     # we set the flag to False! Because we will work with it later!!
                break
        if member_NOT_in_star_wars:     # if he's not in dict,
            if force not in star_wars.keys():   # and if no such key,
                star_wars[force] = [member]     # we create both fresh -> key: [member] <- value is a LIST !!
            else:
                star_wars[force].append(member)     # but if such a key exists, we simply add member to the force
    elif " -> " in current_member:
        member, force = current_member.split(" -> ")
        for key, value in star_wars.items():    # we iterate through EVERY SINGLE VALUE, because they are LISTS !
            if member in value:     # if member anywhere
                if key != force:    # but not in force
                    value.pop(value.index(member))  # we delete him. Now he DOESN'T exist!
        if member_NOT_in_star_wars:     # same as line15 and downwards
            if force not in star_wars.keys():
                star_wars[force] = [member]
            else:
                star_wars[force].append(member)
            print(f"{member} joins the {force} side!")

for force_side, members in star_wars.items():
    if len(members) > 0:
        print(f"Side: {force_side}, Members: {len(members)}")
        for member in members:
            print(f'! {member}')