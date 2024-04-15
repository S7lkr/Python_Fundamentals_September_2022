number = int(input())

for i in range(1, number + 1):
    if i <= 10:
        if i == 5 or i == 7:
            print(f'{i} -> True')
        else:
            print(f'{i} -> False')
    else:
        summ = i // 10 + i % 10
        if summ == 5 or summ == 7 or summ == 11:
            print(f'{i} -> True')
        else:
            print(f'{i} -> False')