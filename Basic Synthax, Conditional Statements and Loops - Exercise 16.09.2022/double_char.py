text = input()
doubled_text = ''

while text != 'End':
    if text == 'SoftUni':
        text = input()
        continue
    for i in text:
        doubled_text += 2 * i
    print(doubled_text)
    doubled_text = ''
    text = input()