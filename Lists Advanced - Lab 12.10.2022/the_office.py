employees = list(map(int, input().split()))
factor = int(input())

overall = [digit * 3 for digit in employees]
average = sum(overall) / len(employees)
happy_count = [value for value in overall if value >= average]

if len(happy_count) >= len(employees) / 2:
    print(f"Score: {len(happy_count)}/{len(employees)}. Employees are happy!")
else:
    print(f"Score: {len(happy_count)}/{len(employees)}. Employees are not happy!")