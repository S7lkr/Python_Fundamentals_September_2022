n = input().split()     # we directly make thr string into a list with the same name: n
number = int(input())   # how many numbers will be removed
digits = list()     # in this list we will
symbols = list()

for ch in n:
    digits.append(int(ch))  # we transform the string list into a new digits list, called 'digits'

for smallest in range(number):  # eliminate 'number'-times the min number from the list
    digits.remove(min(digits))

for digit in digits:
    symbols.append(str(digit))  # the opposite of the 1st for-loop: from digits into a string list
symbols = ', '.join(symbols)    # this makes the list[symbols] into a string, as wanted
print(symbols)