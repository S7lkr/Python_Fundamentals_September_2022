herd = input()
lst = herd.split(', ')
lst.reverse()
animals_checked = 0

for animal in lst:
    animals_checked += 1
    if animal == 'wolf':
        if animals_checked == 1:
            print(f"Please go away and stop eating my sheep")
            break
        else:
            print(f"Oi! Sheep number {animals_checked - 1}! You are about to be eaten by a wolf!")