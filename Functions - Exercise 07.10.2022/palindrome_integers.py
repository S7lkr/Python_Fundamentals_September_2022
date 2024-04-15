def is_palindrome(number):
    for n in number:
        print(n == n[::-1])


num = input().split(', ')
is_palindrome(num)