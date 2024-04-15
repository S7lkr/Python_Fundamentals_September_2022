products = input().split()
wanted_products = input().split()
store = dict()

for index in range(0, len(products), 2):
    key = products[index]
    value = products[index + 1]
    store[key] = value
for product in wanted_products:
    if product in store:
        print(f"We have {store[product]} of {product} left")
    else:
        print(f"Sorry, we don't have {product}")


# letters = {'a': 5, 'b': 10, 'c': 2}
#
# for key, value in letters.items():
#     print(f'{key} - {value}')