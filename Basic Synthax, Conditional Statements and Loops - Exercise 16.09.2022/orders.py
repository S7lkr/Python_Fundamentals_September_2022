orders_cnt = int(input())
final_price = 0

for order_number in range(orders_cnt):
    capsule_price = float(input())
    days = int(input())
    capsule_per_day = int(input())
    price = (capsule_price * capsule_per_day) * days
    if capsule_price < 0.01 or capsule_price > 100:
        continue
    elif days < 1 or days > 31:
        continue
    elif capsule_per_day < 1 or capsule_per_day > 2000:
        continue
    else:
        print(f'The price for the coffee is: ${price:.2f}')
    final_price += price
print(f'Total: ${final_price:.2f}')