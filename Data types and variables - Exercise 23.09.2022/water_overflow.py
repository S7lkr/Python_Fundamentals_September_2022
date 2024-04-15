water_tank_capacity = 255
numbers_of_lines = int(input())
water_tank_litres = 0

for pour in range(numbers_of_lines):
    current_litres = int(input())
    if current_litres + water_tank_litres > water_tank_capacity:
        print('Insufficient capacity!')
        continue
    water_tank_litres += current_litres
print(water_tank_litres)