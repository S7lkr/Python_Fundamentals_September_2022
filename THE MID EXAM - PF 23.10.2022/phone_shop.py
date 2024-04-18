def add(phone, phone_list):
    if phone not in phone_list:
        phone_list.append(phone)
    return phone_list


def remove_it(phone, phone_list):
    if phone in phone_list:
        phone_list.pop(phone_list.index(phone))
    return phone_list


def bonus_phone(old, new, phone_list):
    if old in phone_list:
        phone_list.insert(phone_list.index(old)+1, new)
    return phone_list


def last(phone, phone_list):
    if phone in phone_list:
        phone_list.append(phone_list.pop(phone_list.index(phone)))
    return phone_list


def phone_manager(phone_list):
    while True:
        command = input()
        if command == 'End':
            break
        command = command.split(' - ')
        if command[0] == 'Add':
            phone = command[1]
            phone_list = add(phone, phone_list)
        elif command[0] == 'Remove':
            phone = command[1]
            phone_list = remove_it(phone, phone_list)
        elif command[0] == 'Bonus phone':
            old, new = command[1].split(':')
            phone_list = bonus_phone(old, new, phone_list)
        elif command[0] == 'Last':
            phone = command[1]
            phone_list = last(phone, phone_list)
    print(', '.join(phone_list))


phones = input().split(', ')
phone_manager(phones)


# lst = ['a', 'b', 'c']
# lst.append(lst.pop(lst.index('a')))
# print(lst)