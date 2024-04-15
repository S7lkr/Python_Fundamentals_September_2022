import re

bought_furniture = []
total_money = 0
pattern = r'>>([A-Za-z]+)<<(\d+\.?\d*)!(\d+)'
command = input()
while command != "Purchase":
    match = re.search(pattern, command)
    if match:
        furniture, price, quantity = match.groups()
        bought_furniture.append(furniture)
        total_money += float(price) * int(quantity)
    command = input()
print("Bought furniture:")
for furniture in bought_furniture:
    print(furniture)
print(f"Total money spend: {total_money:.2f}")

# import re
#
# pattern = r">>(\w+)<<(\d+[\.\d]*)!(\d+)"
# text = input()
# total_cost = 0
# print("Bought furniture:")
# while text != "Purchase":
#     sale = re.findall(pattern, text)
#     if sale:
#         furniture = sale[0]
#         print(furniture[0])
#         total_cost += float(furniture[1]) * int(furniture[2])
#     text = input()
# print(f"Total money spend: {total_cost:.2f}")