year = input()
next_year = False
year_found = False

while not year_found:
    if next_year:
        next_year = False
    year = int(year)
    year += 1
    year = str(year)
    for n1 in range(0, len(year)):
        for n2 in range(1, len(year)):
            if n1 == n2 == (len(year) - 1):
                year_found = True
                break
            if year[n1] == year[n2]:
                if n1 != n2:
                    next_year = True
                    break
        if year_found:
            break
        elif next_year:
            break
if year_found:
    print(year)

# # Using set()
# year = int(input())
# year_found = False
#
# while not year_found:
#     year += 1
#     next_year = set()
#     for i in range(len(str(year))):
#         next_year.add(str(year)[i])
#     if len(str(year)) == len(next_year):
#         year_found = True
#         break
# print(year)


# # IMPORTANT! When using indexing, remember text[0], index 0, ALWAYS corresponds to the first letter in the string: '1'
# text = '12345'
# # [i]= '01234' -> text[0] = 1, text[1] = 2, text[2] = 3, text[3] = 4 and text[4] = 5
#
# # NOTE in this for-loop there is NO INDEXING, so it will print: 1,2,3,4, where len(text) = 5, so 5 is EXCLUDED!
# for i in range(1, len(text)):
#     print(i)
#
# # This for-loop has INDEXING. It will start from 1st index -> text[1], which is '2' to '5' (5 included!): 2,3,4,5
# for i in range(1, len(text)):  # NOTE that it will ALWAYS go to the full len(text), LAST SYMBOL '5' INCLUDED!!
#     print(text[i])      # prints all indexes in the string 'text'