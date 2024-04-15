import re

regex = r"\d+"
lines = input()
while lines:
    matches = re.findall(regex, lines)
    if matches:
        print(" ".join(matches), end=" ")
    lines = input()