students = int(input())
lectures = int(input())
bonus = int(input())
points = []
attendances = []

for student in range(students):
    attendance = int(input())
    total_bonus = attendance / lectures * (5 + bonus)
    attendances.append(total_bonus)
    points.append(attendance)

total_lectures = max(points)
max_bonus = max(attendances)

print(f'Max Bonus: {round(max_bonus)}.')
print(f"The student has attended {total_lectures} lectures.")