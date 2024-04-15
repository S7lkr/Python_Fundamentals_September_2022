n = int(input())
word = input()
strings = list()

for string in range(n):
    current_string = input()
    strings.append(current_string)
print(strings)

for i in range(len(strings)-1, -1, -1): # Iterate backwards [3], [2], [1], [0] to avoid index errors!
    element = strings[i]
    if word not in element:
        strings.remove(element)
print(strings)


# n = int(input())
# word = input()
# lst1 = [input() for _ in range(n)]
#
# print(lst1)
# print(list(filter(lambda x: word in x, lst1)))    # print[el for el in lst1 if word in el]