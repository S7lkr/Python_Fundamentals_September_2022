import re

products = input()
total_calories = 0
pattern = r"(#|\|)((?:[A-Z][a-z]+\s?)+)\1(\d{2}\/\d{2}\/\d{2})\1(\d+)\1"
foods = re.findall(pattern, products)

for food in foods:
    total_calories += int(food[3])
days = total_calories // 2000
print(f"You have food to last you for: {days} days!")

[print(f"Item: {item[1]}, Best before: {item[2]}, Nutrition: {item[3]}") for item in foods]