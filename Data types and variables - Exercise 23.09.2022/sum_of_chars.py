loops = int(input())
total_sum = 0

for num in range(loops):
    if loops > 20:
        break
    symbols = ord(input())
    total_sum += symbols
print(f'The sum equals: {total_sum}')