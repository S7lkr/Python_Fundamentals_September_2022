import re

regex = r"(?<=\b_)[a-zA-Z]+\b"
text = input()
matches = re.findall(regex, text)
print(",".join(matches))