numbers = list(map(int, input().split(', ')))
groups = (max(numbers) // 10) + 1

while len(numbers) > 0:
    lower = 0
    upper = 10
    for group in range(1, groups + 1):
        for num in numbers:
            filtered = list(filter(lambda x: lower < x <= upper, numbers))
            print(f'Group of {group}0\'s: {filtered}')
            lower += 10
            upper += 10
            for number in filtered:
                numbers.remove(number)
            break

# lst = [1, 2, 6, 9, 4, 8]
# even = filter(lambda x: x % 2 == 0, lst)
# print(sorted(list(even)))