encrypted_message = input().split()
decrypted_message = []

for word in encrypted_message:
    number = []
    only_word = []
    word_as_symbols = [ch for ch in word]
    for ch in word_as_symbols:
        if ch.isnumeric():
            number.append(ch)
        else:
            only_word.append(ch)
    only_word[0], only_word[-1] = only_word[-1], only_word[0]
    number_to_char = chr(int(''.join(number)))
    only_word.insert(0, number_to_char)
    decrypted_message.append(''.join(only_word))

print(' '.join(decrypted_message))