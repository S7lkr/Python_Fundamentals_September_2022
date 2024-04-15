group = {}      # dict
student = input().split(":")

while len(student) > 1:     # until we have more than one word
    student, idd, course = student[0], student[1], student[2]
    if course not in group.keys():
        group[course] = []  # we create a new key -> course: []
    group[course].append(f'{student} - {idd}')  # but we already have such a course, append its value (list)
    student = input().split(":")

searched_course = student[0].replace("_", " ")  # after exiting the while-loop, we have only 1 word -> index[0]

for person in group[searched_course]:   # this only print the values of the key with 'searched_course' name
    print(person)