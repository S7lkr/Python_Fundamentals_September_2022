first_position = input()
second_position = input()
third_position = input()
lst = [first_position, second_position, third_position]

lst[0], lst[2] = lst[2], lst[0]

print(lst)