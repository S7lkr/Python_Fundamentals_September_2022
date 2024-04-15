chars_count = {}
text = input()

for ch in range(len(text)):
    letter = text[ch]
    if letter == " ":
        continue
    if letter not in chars_count:
        chars_count[letter] = 0
    chars_count[letter] += 1

for key, value in chars_count.items():
    print(f"{key} -> {value}")