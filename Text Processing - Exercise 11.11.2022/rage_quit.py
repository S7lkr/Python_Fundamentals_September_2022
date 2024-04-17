# Regular expressions:
import re

result = []
unique_chars = set()

for match in re.finditer(r"(\D+)(\d+)", input().upper()):
    if match.group(2) == '0':
        continue

    result.append((match.group(1), match.group(2)))

    unique_chars.update(list(match.group(1)))

print(f"Unique symbols used: {len(unique_chars)}")

for pair in result:
    print(pair[0] * int(pair[1]), end="")

# string = input()
# unique_symbols = set()
# rage = []
# text_piece = []
# index = 0
# for ch in string:
#     if ch.isdigit():
#         if string[index+1].isdigit() and int(ch) != 0:
#             two_digit_num = int(ch + string[index+1])
#             rage.append(two_digit_num * "".join(text_piece))
#         rage.append(int(ch) * "".join(text_piece))
#         text_piece.clear()
#     else:
#         unique_symbols.add(ch.upper())
#         text_piece += ch.upper()
#     index += 1
#
# print(f"Unique symbols used: {len(unique_symbols)}")
# print("".join(rage))