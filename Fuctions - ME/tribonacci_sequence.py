def tribonacci(num):
    if num == 0 or num == 1 or num == 2:
        return 1
    elif num == 3:
        return 2
    else:
        return tribonacci(num - 1) + tribonacci(num - 2) + tribonacci(num - 3)


def print_tribonacci(num):
    for i in range(1, num + 1):
        print(tribonacci(i), end=" ")


number = int(input())
print_tribonacci(number)