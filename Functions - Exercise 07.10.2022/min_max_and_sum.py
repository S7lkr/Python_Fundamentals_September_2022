def minimum(nums):
    return f'The minimum number is {min(nums)}'


def maximum(nums):
    return f'The maximum number is {max(nums)}'


def sum_of_numbers(nums):
    return f'The sum number is: {sum(nums)}'


numbers = list(map(int, input().split()))

print(minimum(numbers))
print(maximum(numbers))
print(sum_of_numbers(numbers))