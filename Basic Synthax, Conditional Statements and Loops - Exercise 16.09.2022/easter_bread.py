budget = float(input())
kg_flour_price = float(input())

budget_left = budget
total_breads = 0
total_eggs = 0

pack_eggs_price = 0.75 * kg_flour_price
milk_price = (kg_flour_price + (kg_flour_price * 0.25)) / 4
price_for_single_bread = kg_flour_price + pack_eggs_price + milk_price

while price_for_single_bread <= budget_left:
    total_breads += 1
    budget_left -= price_for_single_bread
    total_eggs += 3
    if total_breads % 3 == 0:
        total_eggs -= total_breads - 2

print(f"You made {total_breads} loaves of Easter bread! Now you have {total_eggs} eggs and {budget_left:.2f}BGN left.")