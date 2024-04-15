name = input()
name_length = 0

while name != 'Welcome!':
    if name == 'Voldemort':
        print("You must not speak of that name!")
        break
    for ch in range(len(name)): # намираме дължината на името
        name_length += 1
    if name_length < 5: # Прайм проверки, кое име, според дължината, къде отива
        print(f"{name} goes to Gryffindor.")
    elif name_length == 5:
        print(f"{name} goes to Slytherin.")
    elif name_length == 6:
        print(f"{name} goes to Ravenclaw.")
    else:
        print(f"{name} goes to Hufflepuff.")
    name_length = 0 # зануляваме дължината на името, да не трупа 15 милиона символи
    name = input()  # въвеждаме ново име, за да почне да върти с вече НОВОТО, различно име
else:
    print("Welcome to Hogwarts.")