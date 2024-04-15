number = input()
lst = list()    # or biggest = []

for num in range(len(number)):
    # using for-loop, we add all characters in 'number' into a list, index by index
    lst.append(number[num])
# we SORT all the contents of the list REVERSED, from biggest to lowest
lst.sort(reverse=True)
# thus, we print all contents together
print(''.join(lst))