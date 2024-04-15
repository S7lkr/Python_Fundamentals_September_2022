string_1 = input()
string_2 = input()
last_printed_string = string_1

for ch in range(1, len(string_1) + 1):
    left = string_2[:ch] # [0:ch:1] -> WE READ: from the START [index 0], to index ch, INCLUDED, with step 1
    right = string_1[ch:]  # [ch:len(string_2):1] -> from [index ch], EXCLUDED, to the end of the string, with step 1
    new_string = left + right
    if new_string == last_printed_string:
        continue
    print(new_string)
    last_printed_string = new_string