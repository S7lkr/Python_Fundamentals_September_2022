n = int(input())
online_register = {}

for driver in range(n):
    command = input().split(" ")
    if command[0] == 'register':
        name, plate_number = command[1], command[2]
        if name not in online_register.keys():
            online_register[name] = plate_number
            print(f"{name} registered {plate_number} successfully")
        else:
            print(f"ERROR: already registered with plate number {plate_number}")
    elif command[0] == "unregister":
        name = command[1]
        if name in online_register.keys():
            online_register.pop(name)
            print(f"{name} unregistered successfully")
        else:
            print(f"ERROR: user {name} not found")

for key, value in online_register.items():
    print(f"{key} => {value}")