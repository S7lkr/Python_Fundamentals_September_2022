employee_eff_1 = int(input())
employee_eff_2 = int(input())
employee_eff_3 = int(input())
students = int(input())
hours = 0
students_per_hour = employee_eff_1 + employee_eff_2 + employee_eff_3

while students > 0:
    hours += 1
    if hours % 4 == 0:
        continue
    else:
        students -= students_per_hour

if students < students_per_hour:
    print(f'Time needed: {hours}h.')