lost_fights = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())

helmet = (lost_fights // 2) * helmet_price
sword = (lost_fights // 3) * sword_price
shield = (lost_fights // 6) * shield_price
armor = (lost_fights // 12) * armor_price
expenses = helmet + sword + shield + armor

print(f"Gladiator expenses: {expenses:.2f} aureus")