def add(p, c, tk):
    if p not in collection.keys():
        collection[p] = [c, tk]
        return f"{p} by {c} in {tk} added to the collection!"
    return f"{p} is already in the collection!"


def remove(p):
    if p in collection.keys():
        del collection[p]
        return f"Successfully removed {p}!"
    return f"Invalid operation! {p} does not exist in the collection."


def change_key(p, nk):
    if p in collection.keys():
        collection[p][1] = nk
        return f"Changed the key of {p} to {nk}!"
    return f"Invalid operation! {p} does not exist in the collection."


number_of_pieces = int(input())
collection = {}

for _ in range(number_of_pieces):
    piece, composer, key = input().split("|")
    collection[piece] = [composer, key]

line = input().split("|")
while line[0] != "Stop":
    command = line[0]
    piece = line[1]
    if command == "Add":
        composer = line[2]
        tone_key = line[3]
        print(add(piece, composer, tone_key))
    elif command == "Remove":
        print(remove(piece))
    elif command == "ChangeKey":
        new_key = line[2]
        print(change_key(piece, new_key))
    line = input().split("|")
for song, value in collection.items():
    print(f"{song} -> Composer: {value[0]}, Key: {value[1]}")