def factorial_divider(num1, num2):
    factorial_1 = 1
    factorial_2 = 1
    for digit in range(2, num1 + 1):
        factorial_1 *= digit
    for digit in range(2, num2 + 1):
        factorial_2 *= digit
    result = factorial_1 / factorial_2
    return f'{result:.2f}'


n1 = int(input())
n2 = int(input())
print(factorial_divider(n1, n2))

# a = (5, 7, 8)
# b = sum(a)