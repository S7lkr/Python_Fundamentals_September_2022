def price(prd, prc):
    if prd == 'coffee':
        return f'{1.5 * quantity:.2f}'
    elif prd == 'water':
        return f"{1 * quantity:.2f}"
    elif prd == 'coke':
        return f'{1.4 * quantity:.2f}'
    elif prd == 'snacks':
        return f'{2 * quantity:.2f}'


product = input()
quantity = int(input())
print(price(product, quantity))