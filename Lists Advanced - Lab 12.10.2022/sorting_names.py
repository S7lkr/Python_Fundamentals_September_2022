names = input().split(', ')

# We use a sorted() function to sort the names by their LENGTH FIRST, and then - alphabetically:
sorted_list = sorted(names, key=lambda name: (-len(name), name))
print(sorted_list)