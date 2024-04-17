text = input().split()
result = 0

for word in text:
    number = int("".join([(word[digit]) for digit in range(1, len(word) - 1)]))
    front_ch = word[0]
    end_ch = word[-1]
    if front_ch.islower():
        number *= ord(front_ch) - 96
    elif front_ch.isupper():
        number /= ord(front_ch) - 64
    if end_ch.islower():
        number += ord(end_ch) - 96
    elif end_ch.isupper():
        number -= ord(end_ch) - 64
    result += number
print(f"{result:.2f}")