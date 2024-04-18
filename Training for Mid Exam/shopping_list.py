def urgent(item, products):
    if item not in products:
        products.insert(0, item)
    return products


def unnecessary(item, products):
    if item in products:
        products.remove(item)
    return products


def correct(old, new, products):
    if old in products:
        for item in range(len(products)):
            if products[item] == old:
                products.pop(item)
                products.insert(item, new)
    return products


def rearrange(item, products):
    if item in products:
        products.append(products.pop(item))
    return products


def shopping_time(products):
    command = input()
    while command != 'Go Shopping!':
        command = command.split()
        item = command[1]
        if command[0] == 'Urgent':
            products = urgent(item, products)
        elif command[0] == 'Unnecessary':
            products = unnecessary(item, products)
        elif command[0] == 'Correct':
            old_item = item
            new_item = command[2]
            products = correct(old_item, new_item, products)
        elif command[0] == 'Rearrange':
            products = rearrange(item, products)
        command = input()
        
    print(', '.join(products))


products_list = input().split('!')
shopping_time(products_list)


# lst = ['book', 'lego', 'pencil', 'guitar']
# old = input()
# new = input()
# for item in range(len(lst)):
#     if lst[item] == old:
#         lst.pop(item)
#         lst.insert(item, new)
# print(lst)