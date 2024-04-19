lst = [1, 2, 'b', 'a', 'g', 3, 2, 2, 'N', 4, 'f', 2, 2, 'P']
lst_2 = ['t', 'u', 'c', 'a', 'R', 'B']

# print(type(lst))    # shows the type of 'lst'. This is LIST!
# print(len(lst))   # shows the length (elements number) of the list
# print(lst[10])    # prints 10th index -> 'f'
# print(lst)


# 1. SORT
# lst_2.sort()              # sorts all elements in the list, starting from small to big: a, b, c.. or 1, 2, 3...
# lst_2.sort(reverse=True)  # same, but backwards. All elements MUST be the same TYPE (int, str) though
# print(sorted(lst_2))      # ONLY shows the SORTED list, but DOES NOT SAVE it as sorted !!


# 2. REVERSE
# lst_2.reverse()   # reverses everything in the exact opposite order. All elements must be the same type: INT or STR!
# print(lst_2)      # very USEFUL TOOL to work with a list backwards, using for-loop!
# print(lst[::-1])  # equal to -> print(reversed(lst))


# 3. APPEND /adds a SINGE element AT THE END of a list/
# lst.append(8)     # adds 8
# print(lst)        # lst += 8 is equivalent


# 4. EXTEND /act the same as APPEND/
# lst.extend("X")
# lst.extend(["NY", 13, "Z"])     # Its real power, though, is you can also add several elements from another list
# print(lst)                      # EXTEND lst with these 3 elements -> [1, 2, b...."NY", 13, "Z"]


# 5. INSERT
# lst.insert(2, 'X')    # insert 'X' AFTER the 2nd index
# print(lst)


# 6. SWAP
# lst[3], lst[5] = lst[5], lst[3]     # changes the positions of indexes 5 and 3
# print(lst)


# 7. REPLACE
# lst[9] = 'S'      # replaces element "4" on index 9, with 'S'
# print(lst)


# 8. POP  -->     Removes an element by its INDEX (NOT by its element name!)
# char = lst.pop()      # pop() removes LAST INDEX, and STORES its value! POP - remove and store its value!
# char_2 = lst.pop(8)   # pops the element on 8th index -> 'N'. You can pop any INDEX you want and store its value
# print(char_2)         # and print it afterwards
# print(lst)


# 9. REMOVE --->  Removes an element by its NAME (NOT BY ITS INDEX!). NOTE: remove -> by element, pop -> by index
# lst.remove(4)     # removes 4 from "lst" on index 9
# lst.remove("g")   # deletes "g"
# print(lst)        # unlike pop, it will NOT store its value, though


# 10. DEL  --->  exactly the same as REMOVE
# del lst[4]  # deletes 4th index -> element: "g"
# print(lst)


# 11. INDEX
# number = lst_2.index("u")   # the index of "u" 'lst_2'
# print(number)               # 2 is on index[1] MET FIRST in the list!


# 12. COUNT
# repetition = lst.count(2)   # shows how many times there are 2-s in list
# print(repetition)           # 5 times


# 13. SPLIT   ->  Adds SEPARATED symbols from a string to list
# text = input()            # you can split ONLY strings
# my_list = text.split()    # NOTE: you should previously know how the symbols in string are separated:
# #  OR SIMPLY
# text = input.split()      # here is split() -> by ALL empty spaces. Or .split(' ') -> one space
# print(my_list)            # But if the input is 1, 2, 3 then it should be .split(', ') by , and space


# 14. JOIN    ->  The opposite of split. Transforms the list into a string. Elements joined by ''
# another_list = ['x', 'y', 'z']        # you can join only str(list) -> all elements in list must be strings
# text = '-'.join(another_list)         # we define that '-' will be between the symbols in the created string
# print(text)


# 15. COMPREHENSION  ->  Takes every element from a list and transforms it into another list, by special criteria
# nums_as_text = input().split()
# nums_as_digits = [int(ch) for ch in nums_as_text]
# #     OR
# # it makes all 'str' elements from 'nums_as_text' into integers. Can also be done with int-float, int->str, etc.
# nums_as_digits = [int(ch) for ch in input().split()]
# print(nums_as_digits)
#
# # for every digit in 'nums_as_digits' take EVERY EVEN number and add it here in this new 'nums_as_even_digits' list
# nums_as_even_digits = [digit for digit in nums_as_digits if digit % 2 == 0]
# print(nums_as_even_digits)


# 16. MAP   ->  very similar to COMPREHENSION. Transforms every single element into a given condition
# text = input().split()
# digits = list(map(int, text))   # remaps every symbol in text into an integer
#   OR JUST
# text = list(map(int, input().split())); print(text)
# print(digits)


# ---------------EXAMPLES------------------:

# # Remove all 2-s from the list:
# while 2 in lst:           # removes one or more duplicating elements from the list. Removes all: 2, 2, 2, 2 ....
#     lst.remove(2)         # NOTE: we remove ELEMENT 2, not INDEX 2 !!
# print(lst)


# # Remove all 2-s from lst, until only one 2 is left in the list:
# while lst.count(2) > 1:   # while the number of 2-s is more than 1:
#     lst.remove(2)   # remove one 2 from list
# print(lst)


# # Find all the indexes containing 2:
# indexes = list()    # first we create an additional list, called 'indexes'. We will go through every symbol in 'lst'
# for index, element in enumerate(lst):   # lst[0] is 1 -> skip, lst[1] is 2 -> so add it to the list 'indexes' etc...
#     if element == 2:                    # on which index from 'lst', we have a symbol 2
#         indexes.append(index)         # every time we find 2, we will add its index (position) to the list (indexes)
# print(indexes)                        # 2 is on indexes: [1, 6, 7, 11, 12]


# # Add a symbol until list length reaches 19:
# while len(lst) < 20:  # add '@'-s until len(lst) becomes 19 symbols
#     lst.append('@')
# print(lst)


# ENUMERATE - VERY IMPORTANT TOOL, DUDE!!
# for i, ch in enumerate(sorted(lst_2)):  # every loop prints -> index - element
#     print(f'Index {i} - {ch}')          # 0 - t, 1 - u, 2 - c....etc