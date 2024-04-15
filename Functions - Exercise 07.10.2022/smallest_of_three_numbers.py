def smallest_number(numbers):
    return min(numbers)


# 3 different integers as input
number_1 = int(input())
number_2 = int(input())
number_3 = int(input())

# we combine all into a list, called 'list(all_numbers)'
all_numbers = [number_1, number_2, number_3]

# we create another var: 'min_number' which WILL CALL our function 'smallest_number()'
min_number = smallest_number(all_numbers)
print(min_number)   # NOTE: in this case we do not call the f in the print!