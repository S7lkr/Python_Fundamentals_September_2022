event_and_value = input().split('|')
energy = 100
coins_left = 100
job_terminated = False

for element in event_and_value:     # every element(iteration) will have exactly 2 ingredients
    if job_terminated:
        break
    element = element.split('-')
    event = element[0]    # on index 0
    value = int(element[1])   # on index 1
    # event, value = element.split('-')   # can also be written: unpack in always 2 elements: index0 and index1
    if event == 'rest':
        old_energy = energy # 90
        energy += value     # 97
        if energy > 100:   # 97
            energy = 100
        print(f"You gained {energy - old_energy} energy.")
        print(f"Current energy: {energy}.")
    elif event == 'order':
        if energy >= 30:
            energy -= 30
            coins_left += value
            print(f"You earned {value} coins.")
        else:
            energy += 50
            print("You had to rest!")
    else:
        if coins_left >= value:
            coins_left -= value
            print(f"You bought {event}.")
        else:
            print(f"Closed! Cannot afford {event}.")
            job_terminated = True

if not job_terminated:
    print("Day completed!")
    print(f"Coins: {coins_left}")
    print(f"Energy: {energy}")