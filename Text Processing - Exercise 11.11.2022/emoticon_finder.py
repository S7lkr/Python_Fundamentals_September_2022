text = input()
# for ch in range(len(text)):
#     emoticon = ""
#     if text[ch] == ":":
#         emoticon += text[ch]
#         emoticon += text[ch + 1]
#         print(emoticon)

emoticon = [print(''.join(text[ch] + text[ch + 1])) for ch in range(len(text)) if text[ch] == ":"]