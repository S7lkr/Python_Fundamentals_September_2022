snowball_amount = int(input())
best_snowball = 0
weight = 0
speed = 0
quality = 0

for snowball in range(snowball_amount):
    snowball_weight = int(input())
    snowball_speed = int(input())
    snowball_quality = int(input())
    current_snowball = (snowball_weight / snowball_speed) ** snowball_quality
    if current_snowball > best_snowball:
        best_snowball = current_snowball
        weight = snowball_weight
        speed = snowball_speed
        quality = snowball_quality
print(f"{weight} : {speed} = {int(best_snowball)} ({quality})")