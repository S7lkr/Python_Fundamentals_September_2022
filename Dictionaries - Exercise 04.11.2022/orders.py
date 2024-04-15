item = input()
overall = {}

while item != "buy":
    product, price, amount = item.split(" ")
    if product not in overall.keys():
        overall[product] = [0, 0]
    overall[product][0] = price
    overall[product][1] += int(amount)
    item = input()

for final_product in overall.keys():
    price = overall[final_product][0]
    quantity = overall[final_product][1]
    overall[final_product] = float(price) * quantity

for key, value in overall.items():
    print(f"{key} -> {value:.2f}")