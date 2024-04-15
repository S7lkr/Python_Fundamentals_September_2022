numbers = list(map(int, input().split(', ')))

# We use a map() function to iterate over the list 'numbers' to find all the EVEN NUMBERS, and add their INDICES
found_indices_or_no = map(lambda x: x if numbers[x] % 2 == 0 else 'no', range(len(numbers)))

# Use the filter function to filter only the indices and print the result:
even_indices = list(filter(lambda a: a != 'no', found_indices_or_no))

print(even_indices)


# numbers = list(map(int, input().split(', ')))
# even_numbers = [digit for digit in range(len(numbers)) if numbers[digit] % 2 == 0]
# print(even_numbers)


# numbers = list(map(int, input().split(', ')))
# even_num_index = []
#
# for num in range(len(numbers)):
#     if numbers[num] % 2 == 0:
#         even_num_index.append(num)
#
# print(even_num_index)