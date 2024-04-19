name_age = {'steven': 50, 'anna': 35, 'john': 18}   # standard way
name_age2 = dict(steven=50, ann=35, john=18)   # alternate way
lst = ['a', '3', 'b', '1', 'c', '7']
lst_as_dict = {}
city = ['Los Angeles', 'Chicago', 'San Francisco']
married = [True, True, False]
name_age_city = {}

print(len(name_age))    # 3
print(name_age.keys())  # show all keys (as list)
print(name_age.values())  # show all values (as list)
print(name_age.items())  # show all items (as TUPLES in a list)

# REMEMBER: Every DICTIONARY consists of 3 elements: Key, Value, Item!
# 'john' -> key
# name_age['john'] -> value. Reads: The dictionary 'name_age' with key 'john'
# 'john': 18 -> item/pair >> key:value

# NOTE: dictionary[key] will show key's VALUE -> dict[key] = value!
print(name_age['steven'])   # 50 (value)
print(name_age["anna"])     # 35 (value)


# 1. Print KEYS:
# cnt = 1
# for name in name_age.keys():
#     if cnt == len(name_age):  # when on final key, do not put ',' after it. Only print the key.
#         print(name)
#     else:
#         print(name, end=', ')
#         cnt += 1


# 2. Print VALUES:
# print(f"Age: ")
# cnt = 1
# for age in name_age.values():
#     if cnt == len(name_age):
#         print(age)
#     else:
#         print(age, end=', ')
#         cnt += 1

# 4. Print ITEMS(PAIRS) -> KEY, VALUE:
# for name, age in name_age.items():
#     print(f'{name} -> {age}', end=' ')


# 5. Check if KEY is in DICTIONARY:
# print(name_age['anna'] in name_age.keys())  # True or False
# if name_age['anna'] in name_age.keys():  # if such a KEY exist in DICT, it will print it
#     print(name_age['anna'])
# print(name_age.get('anna'))  # None or VALUE of the key


# 7. Create a KEY
# if 'eva' not in name_age:
#     name_age['eva'] = 0    # crate a key 'eva' with value '0' {'eva': 0}
# name_age['eva'] = 38    # give it a value
# # 7.1. Rename its VALUE:
# name_age['eva'] = 43   # {'eva': 43}
# name_age['eva'] = 'age not important'   # {'eva': 'age not important'}
# name_age['eva'] = ''    # {'eva': }


# 6. Delete KEY:
# del name_age['steven']  # deletes SELECTED key
# name_age.pop('steven')  # the same
# name_age.popitem()  # deletes LAST ITEM (key: value)
# del name_age    # CAUTION: deletes dictionary 'name_age'


# 8. "Rename" a KEY:
# NOTE: Practically, you cannot rename a key. Create a new one with same value, and delete the old key!
# let's rename the key 'john' to 'billy':
# name_age['billy'] = ''    # first we create the new key 'billy' and give it value: empty string
# name_age['billy'] = name_age['john']    # 'billy's value(age) will take 'john's value(age)
# del name_age['john']    # then we delete the key 'john'
# # or
# name_age['john'].popitem()


# 9. Clear (empty) a DICT:
# name_age.clear()


# 10. Making a LIST into a DICTIONARY:
# for index in range(0, len(lst), 2):   # always step 2!
#     letter = lst[index]
#     number = int(lst[index + 1])
#     lst_as_dict[letter] = number
# print(f'{lst_as_dict}')


# 11. Add a NEW VALUE to a KEY, from lists: city, married
# NOTE: create a NEW DICT! Do not rewrite OLD DICT, for you will lose elements in the list(value)!

# cnt = 0
# for name in name_age.keys():
#     if name not in name_age_city.keys():
#         name_age_city[name] = []
#     name_age_city[name].append(name_age[name])
#     name_age_city[name].append(city[cnt])
#     name_age_city[name].append("Married" if married[cnt] else "Not Married")
#     cnt += 1
# print(name_age_city)


# 12. Nested dictionaries:
# NOTE: the value of the [key] is now a dictionary:
# dict("sam") is new_dict["sam"] with his own key -> new_dict["sam"]["c#"]

# new_dict = {}
# new_dict["sam"] = {}
# new_dict["sam"]["c#"] = []
# new_dict["sam"]["c#"].append(75)
# new_dict["sam"]["c#"].append(60)
# print(new_dict)