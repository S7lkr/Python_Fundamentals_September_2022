numbers = input().split(" ")
string = input()

message = ""
chars = [ch for ch in string]

for number in numbers:
    digit_sum = 0
    for digit in number:
        digit_sum += int(digit)
    index = digit_sum
    if index > len(string) - 1:     # NOTE: len(string)-1 !!!
        index -= len(string)
    ch = chars.pop(index)
    message += ch

print(message)