text = input().split()  # the output is a text, made into a list
bakery = {}     # empty dictionary. Or -> dict()

# now we need to transform the list 'text' into a dict -> {text[0]: text[1], text[2], text[3]...etc.}
# or to create PAIRS -> key: value
# we shall go through all elements in the list 'text'. By INDEX!

for index in range(0, len(text), 2):        # we will for-loop by INDEX with a step 2!
    # bakery[text[index]] = int(text[index + 1])
    key = text[index]         # 'key' will be first part of the pair 'key:value'
    value = int(text[index + 1])       # 'value' will be the second one
    bakery[key] = value     # CONNECT the pair: "bakery" with key [bread] will now have a value 10
                            # by typing bakery[key] automatically we declare that bakery IS a DICTIONARY!

# NOTE: Dictionaries DOES NOT have indexes!! They have KEYS!
# Think of bakery[bread] = 10 as of lst[0] = 'a'
# 'bakery' with key [bread] has a value 10, just like lst with index [0] has an element 'a'

print(bakery)

# print(my_dictionary)
# print(my_dictionary.keys())
# print(my_dictionary.values())
# print(my_dictionary.items())