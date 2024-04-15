words = input().split()

filtered_words = list(filter(lambda x: len(x) % 2 == 0, words))
print('\n'.join(filtered_words))