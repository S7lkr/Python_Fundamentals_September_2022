numbers = input().split(', ')
int_numbers = []
cnt = 0

for num in numbers:
    int_numbers.append(int(num))
while 0 in int_numbers:
    int_numbers.remove(0)
    cnt += 1
for zero in range(cnt):
    int_numbers.append(0)

print(int_numbers)