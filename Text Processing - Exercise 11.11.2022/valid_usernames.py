def length_valid(checked_word):
    if 3 <= len(checked_word) <= 16:
        return True
    return False


def is_only_letters_digits(checked_word):
    if checked_word.isalnum() or "-" in checked_word or "_" in checked_word:
        return True
    return False


def no_redundant_symbols(checked_word):
    if "<" in checked_word or ">" in checked_word or "=" in checked_word:
        return False
    return True


text = input().split(", ")
for word in text:
    if not length_valid(word):
        continue
    if not is_only_letters_digits(word):
        continue
    if not no_redundant_symbols(word):
        continue
    print(word)