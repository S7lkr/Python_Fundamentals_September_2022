def max_num(all_max_num):
    if not all_max_num:
        return 'No matches'
    elif result.count(max(all_max_num)) > 1:
        rightmost_index = [i for i in range(len(result)) if result[i] == all_max_num]
        return rightmost_index[-1]
    else:
        max_number = max(all_max_num)
        return result.index(max_number)


def min_num(all_min_num):
    if not all_min_num:
        return 'No matches'
    elif result.count(min(all_min_num)) > 1:
        rightmost_index = [i for i in range(len(result)) if result[i] == all_min_num]
        return rightmost_index[-1]
    else:
        min_number = min(all_min_num)
        return result.index(min_number)


def first_numbers(nums):
    if nums:
        first_even = nums[:count]
        return first_even
    else:
        return '[]'


def last_numbers(nums):
    if nums:
        last_even = nums[len(nums) - count:]
        return last_even
    else:
        return '[]'


integers = input().split(" ")
result = list(map(int, integers))

command = input().split(" ")
while command[0] != 'end':
    action = command[0]
    if action == 'exchange':
        index = int(command[1])
        if 0 <= index < len(result):
            left = result[:index + 1]
            right = result[index + 1:]
            result = list(map(int, right + left))
        else:
            print('Invalid index')
    elif action == 'max':
        if command[1] == 'even':
            all_max_even_num = list(filter(lambda x: x % 2 == 0, result))
            print(max_num(all_max_even_num))
        elif command[1] == 'odd':
            all_max_odd_num = list(filter(lambda x: x % 2 != 0, result))
            print(max_num(all_max_odd_num))
    elif action == 'min':
        if command[1] == 'even':
            all_min_even_num = list(filter(lambda x: x % 2 == 0, result))
            print(min_num(all_min_even_num))
        elif command[1] == 'odd':
            all_min_odd_num = list(filter(lambda x: x % 2 != 0, result))
            print(min_num(all_min_odd_num))
    elif action == 'first':
        count = int(command[1])
        if 0 < count <= len(result):
            if command[2] == 'even':
                all_even = [i for i in result if i % 2 == 0]
                print(first_numbers(all_even))
            elif command[2] == 'odd':
                all_odd = [i for i in result if i % 2 != 0]
                print(first_numbers(all_odd))
        else:
            print('Invalid count')
    elif action == 'last':
        count = int(command[1])
        if 0 < count <= len(result):
            if command[2] == 'even':
                all_even = [i for i in result if i % 2 == 0]
                print(last_numbers(all_even))
            elif command[2] == 'odd':
                all_odd = [i for i in result if i % 2 != 0]
                print(last_numbers(all_odd))
        else:
            print('Invalid count')
    command = input().split(" ")

print(result)