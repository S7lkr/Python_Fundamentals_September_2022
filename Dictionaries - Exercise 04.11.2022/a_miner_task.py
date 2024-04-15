resource = input()
collection_of_resources = {}

while resource != 'stop':
    quantity = int(input())
    if resource not in collection_of_resources.keys():
        collection_of_resources[resource] = 0
    collection_of_resources[resource] += quantity
    resource = input()

for resource, quantity in collection_of_resources.items():
    print(f'{resource} -> {quantity}')