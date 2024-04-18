import re

text = input()
emoji_pattern = r"(\:{2}|\*{2})([A-Z][a-z]{2,})(\1)"
emoji_match = re.findall(emoji_pattern, text)

threshold = re.findall(r"\d", text)
coolness = list(map(int, threshold))

total_coolness = 1
for digit in coolness:
    total_coolness *= digit
print(f"Cool threshold: {total_coolness}")

print(f" {len(emoji_match)} emojis found in the text. The cool ones are:")
for emoji in emoji_match:
    counter = [ord(ch) for ch in emoji[1]]
    if sum(counter) > total_coolness:
        print("".join(emoji))