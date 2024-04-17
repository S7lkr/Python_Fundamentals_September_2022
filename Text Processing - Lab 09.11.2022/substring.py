remove_word = input()
some_string = input()
while remove_word in some_string:
     some_string = some_string.replace(remove_word, "")  # NOTE: replace 'ice' in 'some_string' with ''(empty str)
print(some_string)