dungeons = input().split('|')
health = 100
coins = 0
rooms = 0
game_over = False

for room in dungeons:
    event, value = room.split(' ')
    rooms += 1
    if event == 'potion':
        hp_left = health
        hp_gained = value
        health += int(value)
        if health > 100:
            hp_gained = 100 - hp_left
            health = 100
        print(f'You healed for {hp_gained} hp.')
        print(f'Current health: {health} hp.')
    elif event == 'chest':
        coins += int(value)
        print(f"You found {value} bitcoins.")
    else:
        health -= int(value)
        if health > 0:
            print(f"You slayed {event}.")
        else:
            print(f"You died! Killed by {event}.")
            print(f"Best room: {rooms}")
            game_over = True
            break

if not game_over:
    print(f"You've made it!")
    print(f"Bitcoins: {coins}")
    print(f"Health: {health}")