store = {}
product_quantity = input()

while product_quantity != 'statistics':
    product, quantity = product_quantity.split(': ')
    if product not in store.keys():
        store[product] = 0
    store[product] += int(quantity)
    product_quantity = input()

print("Products in stock:")
for (product, quantity) in store.items():
    print(f'- {product}: {quantity}')
# [print(f"- {product}: {quantity}") for (product, quantity) in store]

print(f"Total Products: {len(store)}")
print(f"Total Quantity: {sum(store.values())}")