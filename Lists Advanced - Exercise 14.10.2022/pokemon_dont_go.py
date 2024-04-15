numbers = list(map(int, input().split(" ")))
total_distance = []

while numbers:
    index = int(input())
    element = 0
    if index < 0:
        element = numbers.pop(0)
        last = numbers[-1]
        numbers.insert(0, last)
    elif index >= len(numbers):
        element = numbers.pop()
        first = numbers[0]
        numbers.append(first)
    else:
        element = numbers.pop(index)
    for curr_index in range(len(numbers)):
        if numbers[curr_index] <= element:
            numbers[curr_index] += element
        else:
            numbers[curr_index] -= element
    total_distance.append(element)

print(sum(total_distance))