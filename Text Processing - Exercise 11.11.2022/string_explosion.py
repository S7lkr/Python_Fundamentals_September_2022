text = input()
result = ""
explosion_power = 0
index = 0
print(result)

for ch in text:
    if ch == ">":
        next_ch = text[index + 1]
        if next_ch.isdigit():
            explosion_power += int(next_ch)
        result += ch
    elif explosion_power < 1:
        result += ch
    else:
        explosion_power -= 1
    index += 1
print(result)