def add_stop(ind, st, way):
    if 0 <= ind <= len(way) - 1:
        way = way[:ind] + st + way[ind:]
        return way
    return way


def remove_stop(start, end, way):
    if 0 <= start <= len(way) - 1 and end <= len(way) - 1:
        part = way[start:end + 1]
        way = way.replace(part, "")
        return way
    return way


def switch(old_str, new_str, way):
    if old_str in way:
        way = way.replace(old_str, new_str)
        return way
    return way


route = input()
command = input().split(":")

while command[0] != "Travel":
    index = command[1]
    if command[0] == "Add Stop":
        string = command[2]
        route = add_stop(int(index), string, route)
    elif command[0] == "Remove Stop":
        start_index = int(command[1])
        end_index = int(command[2])
        route = remove_stop(start_index, end_index, route)
    elif command[0] == "Switch":
        old_string = command[1]
        new_string = command[2]
        route = switch(old_string, new_string, route)
    print(route)
    command = input().split(":")

print(f"Ready for world tour! Planned stops: {route}")