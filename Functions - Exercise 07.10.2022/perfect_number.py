def perfect_num(num):
    divisors_sum = 0
    for divisor in range(1, (num // 2) + 1):
        if num % divisor == 0:
            divisors_sum += divisor
    if divisors_sum == num:
        print('We have a perfect number!')
    else:
        print('It\'s not so perfect.')


number = int(input())
perfect_num(number)