# 1. "For-loop":
# text = input()
# output = ""
# for index in range(len(text)):
#     if index == len(text)-1:
#         output += text[index]
#         break
#     elif text[index] != text[index + 1]:
#         output += text[index]
# print(output)

# 2. "While-loop":
text = input()
output = ""
index = 0
while index < len(text) - 1:
    if text[index] != text[index + 1]:
        output += text[index]
    index += 1
    continue
if index == len(text) - 1:
    output += text[index]
print(output)
