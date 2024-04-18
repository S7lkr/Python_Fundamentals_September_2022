people = int(input())
lift = list(map(int, input().split()))

for wagon in range(len(lift)):
    if people >= 4:
        diff = 4 - lift[wagon]
        lift[wagon] += diff
        people -= diff
    else:
        lift[wagon] += people
        people = 0

if people > 0:
    print(f"There isn't enough space! {people} people in a queue!")
if lift[-1] < 4:
    print(f"The lift has empty spots!")

print(' '.join(map(str, lift)))