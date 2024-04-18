food_gr = float(input()) * 1000
hay_gr = float(input()) * 1000
cover_gr = float(input()) * 1000
weight_gr = float(input()) * 1000
supplies_over = False
month_over = False

while not supplies_over:
    if month_over:
        break
    for day in range(1, 31):
        if food_gr <= 300 or hay_gr <= 0 or cover_gr <= 0:
            supplies_over = True
            break
        food_gr -= 300
        if day % 2 == 0:
            hay_gr -= 0.05 * food_gr
        if day % 3 == 0:
            cover_gr -= weight_gr / 3
        if day == 30:
            month_over = True
            break

if supplies_over:
    print("Merry must go to the pet store!")
else:
    print(f"Everything is fine! Puppy is happy! Food: {food_gr / 1000:.2f}, Hay: {hay_gr / 1000:.2f}, "
          f"Cover: {cover_gr / 1000:.2f}.")