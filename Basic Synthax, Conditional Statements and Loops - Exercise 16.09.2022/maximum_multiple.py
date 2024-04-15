divisor = int(input())
boundary = int(input())

# result = (boundary // divisor) * divisor
# print(result)

for current_number in range(boundary, divisor, -1):
    if current_number % divisor == 0:
        print(current_number)
        break