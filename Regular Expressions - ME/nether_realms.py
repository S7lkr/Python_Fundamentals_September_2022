import re

line = input()
demons = re.split(r"\s*,\s*", line)
demon_dict = {}
for demon_name in demons:
    health_points = 0
    damage_points = 0
    hp_pattern = r"[^0-9\+\-\*\/\.]"
    letters_found = re.findall(hp_pattern, demon_name)
    for ch in letters_found:
        health_points += ord(ch)
    damage_pattern = r"((?:\-|\+)?\d+(?:\.\d+)*)"
    damage_points = re.findall(damage_pattern, demon_name)
    damage_points = sum(list(map(float, damage_points)))
    for symbol in demon_name:
        if symbol == "*":
            damage_points *= 2
        elif symbol == "/":
            damage_points /= 2
    demon_dict[demon_name] = [health_points, damage_points]
for key, value in sorted(demon_dict.items()):
    print(f"{key} - {value[0]} health, {value[1]:.2f} damage")