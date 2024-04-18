import re

text = input()
pattern = r"(@|#)([A-Za-z]{3,})\1{2}([A-Za-z]{3,})"
matches = re.findall(pattern, text)
if matches:
    print(f"{len(matches)} word pairs found!")
else:
    print("No word pairs found!")

mirror_words = [f"{match[1]} <=> {match[2]}" for match in matches if match[1] == match[2][::-1]]
if mirror_words:
    print(f"The mirror words are:\n{', '.join(mirror_words)}")
else:
    print("No mirror words!")
