n = int(input())
word_with_synonym = {}

for word in range(n):
    key = input()
    value = input()
    if key not in word_with_synonym.keys():
        word_with_synonym[key] = []
    word_with_synonym[key].append(value)

for key, value in word_with_synonym.items():
    print(f'{key} - {", ".join(value)}')