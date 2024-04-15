def odd_even_sum(num):
    odd_sum = [int(digit) for digit in num if int(digit) % 2 != 0]
    even_sum = [int(digit) for digit in num if int(digit) % 2 == 0]
    return f'Odd sum = {sum(odd_sum)}, Even sum = {sum(even_sum)}'


number = input()
print(odd_even_sum(number))

# number = '18392'
# lst = [int(num) for num in number if int(num) % 2 == 0]
# print(sum(lst))