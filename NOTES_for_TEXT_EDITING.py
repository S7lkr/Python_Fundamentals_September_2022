# REMEMBER! Slicing works ONLY with INDEXES!

text = '123456789'
# # text[0], text[1], text[2]... GET element by its index --> 1, 2, 3

# To slice something, we need a START-point and END-point -> text[0:3] /or text[:3]/ -> 0 - start, 3 - end.
# So text[:3] will slice "123" -> index 0, 1, 2. REMEMBER: Index 3 WILL NOT BE TAKEN !!!!
# NOTE: The START index is INCLUSIVE! The END index is EXCLUSIVE!

# # When printing backwards, bear in mind, if u want to start from EXACTLY the last element -> '9' in '123456789',
# # u need to type the range:

# for ch in range(len(text) - 1, -1, -1):     # --> iterate every element in "text" BACKWARDS
#     print(ch)

        # OR shorter:


# text = text[::-1]
# print(text)
# print(text[len(text)-1])    # text[-1] -> with index LENGTH of TEXT minus 1, which is 8 (last index)
# REMEMBER: text[8] = text[len(text)-1] !!!

# WHY len(text)-1 ?
# Because len(text) = 9. All indexes are: 0,1,2,3,4,5,6,7,8 (total of 9). LAST INDEX -> text[8] or text[-1]

# print(len(text)) -> the LENGTH of "text" (how many elements)
# print(text[1:4])    # equal to 'text[1:4:1] -> 234 -> from index 1 to 4th with step 1

# print(text[:3], text[3:6], text[6::])     # 123 456 789
# NOTE: if it was: text[::3] --> with step 3, prints: 147

# print(text[0] + text[8] + text[3] + text[2])  # this will print all 3 index together -> 1943
# print(text[::-1])   # OR 'text[len(text)-1, -1, -1]'. It will print backwards -> 987....321

# print(text[0:2])       # from start to index 2 (EXCLUSIVE!!) -> 12 -> only indexes [0] and [1]
# print(text[0::2])    # from index 0 to the last, with step 2 -> 13579

# print(text[:-2])    # from start to before-last -> 1,2,3,4,5,6,7,8
# print(text[::-2])   # in the opposite with step 2 -> 97531

# print(text[1::2])   # forward, step 2, starting form [index 1] -> 2468
# print(text[len(text) - 2::-2])  # backwards, step 2