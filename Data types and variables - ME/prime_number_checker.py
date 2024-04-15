number = int(input())   # take a random number

if number > 1:  # the number MUST BE GREATER THAN 1 to initiate the for-loop process!
    for divider in range(2, int(number/2) + 1): # we go through ALL DIVIDERS of the number (if it has any!), and...
        if number % divider == 0:   # if the number has ONLY ONE divider, that divides num without reminder..
            print(False)    # then we are sure the number IS NOT PRIME (is not simple). Therefore, it is COMPLEX!
            break   # we BREAK immediately after submitting the number is complex
    else:   # if the loop is not initiated (meaning the number is PRIME without doubt), we break
        print(True)
else:   # If it is '<=1' it is definitely NOT PRIME (it is COMPLEX), and the code won't start!
    print(False)

# ALL PRIME NUMBERS:
# 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109...