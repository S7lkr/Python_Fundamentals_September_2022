def add(lesson):
    if lesson not in lessons:
        lessons.append(lesson)
    return lessons


def insert_it(lesson, ind):
    if lesson not in lessons:
        lessons.insert(ind, lesson)
    return lessons


def remove_it(lesson):
    if lesson in lessons:
        lessons.remove(lesson)
    return lessons


def swap_it(lesson1, lesson2):
    if (lesson1 and lesson2) in lessons:
        ind_1 = lessons.index(lesson1)
        ind_2 = lessons.index(lesson2)
        lessons[ind_1], lessons[ind_2] = lessons[ind_2], lessons[ind_1]
    for element in lessons:
        if "-Exercise" in element:
            less, ex = element.split("-")
            lessons.insert(lessons.index(less) + 1, lessons.pop(lessons.index(element)))
    return lessons


def exercise(lesson):
    if lesson in lessons:
        lessons.append(f"{lesson}-Exercise")
    else:
        lessons.append(lesson)
        lessons.append(f"{lesson}-Exercise")
    return lessons


lessons = input().split(", ")
command = input()

while command != "course start":
    command = command.split(":")
    act = command[0]
    title = command[1]
    if act == "Add":
        lessons = add(title)
    elif act == "Insert":
        index = int(command[2])
        lessons = insert_it(title, index)
    elif act == "Remove":
        lessons = remove_it(title)
    elif act == "Swap":
        title_2 = command[2]
        lessons = swap_it(title, title_2)
    elif act == "Exercise":
        lessons = exercise(title)
    command = input()

[print(f"{index+1}.{lessons[index]}") for index in range(len(lessons))]