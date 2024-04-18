numbers = list(map(int, input().split()))
average = sum(numbers) / len(numbers)
top_5 = []

for num in numbers:
    if num > average:
        top_5.append(num)
top_5.sort(reverse=True)

while len(top_5) > 5:
    top_5.pop()

if len(top_5) == 0:
    print('No')
else:
    print(" ".join(list(map(str, top_5))))