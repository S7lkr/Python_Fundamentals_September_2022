numbers = input().split()
float_numbers = list(map(float, numbers))   # mapping
float_numbers = [abs(num) for num in float_numbers]     # comprehension
print(float_numbers)