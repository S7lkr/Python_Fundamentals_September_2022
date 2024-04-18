all_targets = list(map(int, input().split()))
shoot_index = input()
targets_eliminated = 0


while shoot_index != 'End':
    shoot_index = int(shoot_index)
    if shoot_index >= len(all_targets):
        shoot_index = input()
        continue
    target_shot = all_targets[shoot_index]
    if target_shot == -1:
        continue
    all_targets[shoot_index] = -1
    targets_eliminated += 1
    for other_target in range(len(all_targets)):
        t = all_targets[other_target]
        if t == -1:
            continue
        elif t <= target_shot:
            all_targets[other_target] += target_shot
        else:
            all_targets[other_target] -= target_shot
    shoot_index = input()

print(f"Shot targets: {targets_eliminated} -> {' '.join(list(map(str, all_targets)))}")