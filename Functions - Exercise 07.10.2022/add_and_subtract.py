# This func. will sum two n1 and n2
def sum_numbers(first, second):
    return first + second


# this, from THE ABOVE RESULT will subtract 'n3'
def subtract(sum_of_the_two, third):
    return sum_of_the_two - third


# this function ONLY calls the other two and gives them 3 arguments!
# NOTE: we cannot call the other funcs, without calling this one, because they are dependent on this one!
def add_and_subtract(n1, n2, n3):               # ALL PARAMETERS from this func, MUST BE GIVEN to the other funcs.
    sum_first_two = sum_numbers(n1, n2)         # n1 and n2 are given to 'sum_numbers()' - DONE
    result = subtract(sum_first_two, n3)        # the RESULT of the 1st func. will ACT AS A PARAMETER to the 2nd f.
    return result                               # so the second func. will take 'sum_first_two' and 'n3' as parameters


number_1 = int(input())
number_2 = int(input())
number_3 = int(input())
# Now, what we ONLY need PRINTED is the final result
print(add_and_subtract(number_1, number_2, number_3))