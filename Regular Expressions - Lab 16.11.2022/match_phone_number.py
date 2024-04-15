import re

phone_numbers = input()
regex = r"(\+359-2-222-2222\b|\+359 2 222 2222)\b"
matches = re.findall(regex, phone_numbers)
print(", ".join(matches))