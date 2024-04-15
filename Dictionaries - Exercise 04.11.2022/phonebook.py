phonebook = {}
name_phone = input()

while not name_phone.isdigit():
    name, phone = name_phone.split("-")
    if name not in phonebook.keys():
        phonebook[name] = ''
    phonebook[name] += phone
    name_phone = input()
# print(phonebook)

for _ in range(int(name_phone)):
    searched_name = input()
    if searched_name not in phonebook:
        print(f"Contact {searched_name} does not exist.")
    else:
        result = {f'{searched_name} -> {phonebook[searched_name]}' for key, value in phonebook.items()}
        print(''.join(result))