total_price_no_tax = 0
total_price_with_taxes = 0
only_taxes = 0
final_price_discount = 0
invalid_price_met = False

while True:
    price = input()
    if price == 'regular' or price == 'special':
        break
    price = float(price)
    if price < 0:
        print('Invalid price!')
        invalid_price_met = True
        continue
    total_price_no_tax += price
    only_taxes += 0.2 * price
total_price_with_taxes = total_price_no_tax + only_taxes
final_price_discount = total_price_with_taxes - (total_price_with_taxes * 0.1)

if total_price_with_taxes <= 0:
    print('Invalid order!')
else:
    print(f"Congratulations you've just bought a new computer!")
    print(f'Price without taxes: {total_price_no_tax:.2f}$\nTaxes: {only_taxes:.2f}$\n-----------')
    if price == 'regular':
        print(f'Total price: {total_price_with_taxes:.2f}$')
    else:
        print(f'Total price: {final_price_discount:.2f}$')