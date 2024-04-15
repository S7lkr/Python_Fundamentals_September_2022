n1 = int(input())
n2 = int(input())
n3 = int(input())

numbers_lst = [n1, n2, n3]
if 0 in numbers_lst:
    print("zero")
    exit()
cnt = 0
for num in numbers_lst:
    if num < 0:
        cnt += 1

if cnt % 2 == 0:
    print("positive")
else:
    print("negative")