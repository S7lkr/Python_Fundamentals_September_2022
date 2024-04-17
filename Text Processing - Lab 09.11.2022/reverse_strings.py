text = input()
while text != "end":
    # print(text + "=" + text[::-1])
    reversed_text = ''
    for letter in range(len(text)-1, -1, -1):
        reversed_text += text[letter]
    print(text + "=" + reversed_text)
    text = input()