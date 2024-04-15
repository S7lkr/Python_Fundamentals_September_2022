import re

racers = input().split(", ")
command = input()
final_score = {}

while command != 'end of race':
    racer_pattern = r"[a-zA-Z]+"
    racer_name = re.findall(racer_pattern, command)
    racer_name = "".join(racer_name)
    if racer_name in racers:
        points_pattern = r"\d"
        racer_points = re.findall(points_pattern, command)
        racer_points = list(map(int, racer_points))
        points = sum(racer_points)
        if racer_name not in final_score.keys():
            final_score[racer_name] = 0
        final_score[racer_name] += points
    command = input()
racers.clear()
for key, value in sorted(final_score.items(), key=lambda item: item[1], reverse=True):
    racers.append(key)
print(f"1st place: {racers[0]}")
print(f"2nd place: {racers[1]}")
print(f"3rd place: {racers[2]}")