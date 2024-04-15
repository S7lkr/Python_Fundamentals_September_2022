text_1 = input().split(', ')
text_2 = input().split(', ')
are_in = []

for word1 in text_1:
    for word2 in text_2:
        if word1 in word2:
            are_in.append(word1)
            break
print(are_in)