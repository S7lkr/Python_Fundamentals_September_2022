def buy_item(cost, money):
    if price <= money:
        money -= price
        purchased.append(price)
    return money


items_with_price = input().split('|')
budget = float(input())

purchased = []
new_prices = []
money_left = budget

for items in items_with_price:
    item, price = items.split('->')
    price = float(price)
    if item == 'Clothes' and price <= 50:
        money_left = buy_item(price, money_left)
    elif item == 'Shoes' and price <= 35:
        money_left = buy_item(price, money_left)
    elif item == 'Accessories' and price <= 20.5:
        money_left = buy_item(price, money_left)

for item in purchased:
    item += item * 0.4
    new_prices.append(item)
profit = sum(new_prices) - sum(purchased)

print(" ".join([f'{value:.2f}' for value in new_prices]))
print(f'Profit: {profit:.2f}')

if money_left + sum(new_prices) >= 150:
    print('Hello, France!')
else:
    print('Not enough money.')
