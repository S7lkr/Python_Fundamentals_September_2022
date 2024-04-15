import re

pattern_1 = r"\b(?P<Day>\d{2})([-.\/])(?P<Month>[A-Z][a-z]{2})\2(?P<Year>\d{4})\b"
dates = input()
matches = re.findall(pattern_1, dates)

for match in matches:
    print(f"Day: {match[0]}, Month: {match[2]}, Year: {match[3]}")