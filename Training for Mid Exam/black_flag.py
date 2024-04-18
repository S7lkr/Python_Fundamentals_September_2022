days = int(input())
daily_plunder = int(input())
expected_plunder = float(input())
total_gained = 0
goal_achieved = False

for day in range(1, days + 1):
    total_gained += daily_plunder
    if day % 3 == 0:
        total_gained += 0.5 * daily_plunder
    if day % 5 == 0:
        total_gained -= total_gained * 0.3
    if total_gained >= expected_plunder:
        goal_achieved = True

if goal_achieved:
    print(f"Ahoy! {total_gained:.2f} plunder gained.")
else:
    percentage = (total_gained / expected_plunder) * 100
    print(f"Collected only {percentage:.2f}% of the plunder.")