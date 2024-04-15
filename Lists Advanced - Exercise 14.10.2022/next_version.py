old_version = list(map(int, input(). split('.')))
new_version = []

for digit in range(len(old_version)-1, -1, -1):
    if old_version[digit] < 9:
        old_version[digit] += 1
        break
    else:
        old_version[digit] = 0
        continue

print('.'.join(map(str, old_version)))