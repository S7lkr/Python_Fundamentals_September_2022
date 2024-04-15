words = input().split(' ')
my_dictionary = {}

for word in words:
    word_low = word.lower()
    if word_low not in my_dictionary:
        my_dictionary[word_low] = 0
    my_dictionary[word_low] += 1

for key, value in my_dictionary.items():
    if value % 2 != 0:
        print(key, end=' ')