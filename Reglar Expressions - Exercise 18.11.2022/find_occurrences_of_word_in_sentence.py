import re

text = input()
word = input()
regex = fr"(?i)\b{word}\b"  # (?i) --> CASE-INSENSITIVE. Always at the start of the regex!
matches = re.findall(regex, text)
print(len(matches))     # with re.findall we always receive a list
