import re

text = input()
pattern = r"(=|/)([A-Z][A-Za-z]{2,})\1"
matches = re.finditer(pattern, text)
destinations = []
travel_points = 0
for match in matches:
    destinations.append(match.group(2))
    travel_points += len(match.group(2))
print(f"Destinations: {', '.join(destinations)}")
print(f"Travel Points: {travel_points}")