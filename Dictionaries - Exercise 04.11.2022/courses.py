courses = input()
student_group = {}

while courses != 'end':
    course, name = courses.split(" : ")
    if course not in student_group.keys():
        student_group[course] = []
    student_group[course].append(name)
    courses = input()

for key, value in student_group.items():
    print(f"{key}: {len(value)}")
    for name in range(len(value)):
        print(f"-- {value[name]}")