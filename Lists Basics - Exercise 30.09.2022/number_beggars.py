money_for_donate = input().split(', ')
beggars_cnt = int(input())
final_sums = list()
money_for_donate_in_digits = []

for element in money_for_donate:
    money_for_donate_in_digits.append(int(element))

for beggar in range(1, beggars_cnt + 1):
    money_for_current_beggar = 0
    for summ in range(beggar-1, len(money_for_donate_in_digits), beggars_cnt):
        money_for_current_beggar += money_for_donate_in_digits[summ]
    final_sums.append(money_for_current_beggar)
print(final_sums)