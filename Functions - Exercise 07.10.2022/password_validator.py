def validator(word):
    error_messages = []
    # password_is_valid = True
    if not (6 <= len(word) <= 10):
        # password_is_valid = False
        # print("Password must be between 6 and 10 characters")
        error_messages.append("Password must be between 6 and 10 characters")
    if not word.isalnum():
        # password_is_valid = False
        # print('Password must consist only of letters and digits')
        error_messages.append('Password must consist only of letters and digits')
    digit_cnt = 0
    for ch in word:
        if ch.isdigit():
            digit_cnt += 1
    if digit_cnt < 2:
        # password_is_valid = False
        # print("Password must have at least 2 digits")
        error_messages.append("Password must have at least 2 digits")
    # return password_is_valid
    return error_messages


password = input()
password_check = validator(password)    # remember to create a VARIABLE for easier work with funcs.

if len(password_check) == 0:
    print('Password is valid')
else:
    print('\n'.join(password_check))

# We have used 2 methods to solve this problem:

# 1.
# Setting a boolean 'password_is_valid' first. So for EACH IF-ELSE CHECK, we set it to FALSE only if
# the condition is met, and immediately print the corresponding message.
# In the end if NOT EVEN ONE if-else is met, that means 'password_is_valid' will still be True (unchanged)
# Therefore, it means that not error messages are met and only 'password is valid' is printed

# 2.
# Creating an empty list 'error_messages'
# Fill the list with corresponding print ONLY IF the if-else check is met.
# If no if-else is met, list will remain EMPTY. If so, print 'password is valid'