n = int(input())
numbers = []

for num in range(n):
    current_number = int(input())
    numbers.append(current_number)

command = input()

if command == 'even':
    for num in range(len(numbers)-1, -1, -1):
        if numbers[num] % 2 != 0:
            numbers.remove(numbers[num])
elif command == 'odd':
    for num in range(len(numbers)-1, -1, -1):
        if numbers[num] % 2 == 0:
            numbers.remove(numbers[num])
elif command == 'negative':
    for num in range(len(numbers)-1, -1, -1):
        if numbers[num] >= 0:
            numbers.remove(numbers[num])
elif command == 'positive':
    for num in range(len(numbers)-1, -1, -1):
        if numbers[num] < 0:
            numbers.remove(numbers[num])
print(numbers)


# def adding_numbers_to_list(a):
#     numbers = [int(input()) for _ in range(a)]
#     text = input()
#
#     requirements = {
#         "even": lambda x: x % 2 == 0,
#         "odd": lambda x: x % 2 == 1,
#         "positive": lambda x: x >= 0,
#         "negative": lambda x: x < 0
#     }
#     return list(filter(requirements[text], numbers))
#
#
# m = int(input())
# print(adding_numbers_to_list(m))