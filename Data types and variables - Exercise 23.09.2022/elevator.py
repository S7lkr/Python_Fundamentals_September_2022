people = int(input())
elevator_capacity = int(input())

courses = people // elevator_capacity
additional = people % elevator_capacity

if additional != 0:
    courses += 1

print(courses)