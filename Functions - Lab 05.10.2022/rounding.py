def round_floats(numbers):
    float_nums = list(map(float, nums))
    rounded = list(map(round, float_nums))
    return rounded


nums = input().split()
print(round_floats(nums))