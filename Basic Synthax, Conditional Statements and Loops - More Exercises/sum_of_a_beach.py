text = input()
word = ''
word_cnt = 0

for ch in text.lower():
    word += ch
    if 'sand' in word or 'water' in word or 'fish' in word or 'sun' in word:
        word_cnt += 1
        word = ''
print(word_cnt)