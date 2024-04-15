number_of_students = int(input())
students_grade = {}

for current_student in range(number_of_students):
    student = input()
    grade = float(input())
    if student not in students_grade.keys():
        students_grade[student] = []
    students_grade[student].append(grade)

for person in students_grade.keys():
    average_grade = sum(students_grade[person]) / len(students_grade[person])
    students_grade[person] = average_grade

for key, value in students_grade.items():
    if value >= 4.50:
        print(f"{key} -> {value:.2f}")
