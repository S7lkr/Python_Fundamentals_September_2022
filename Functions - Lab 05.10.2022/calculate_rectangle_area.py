# This is a function. It is a functionality tool, which requires parameters -> (a, b) or more parameters.
# Every parameter is taken from the argument, which should be described whenever calling the function (line 9).
# When finished with the operations inside the function, we need to store the final result (variable) with 'return'
# Return acts as a 'break' within a for/while loop, but remembers the final result
# We can return a single value, a string, a list, tuple, boolean...etc. it is stored inside the function

def rectangle_area(a, b):
    result = a * b
    return result


side_a = int(input())
side_b = int(input())
print(rectangle_area(side_a, side_b))
# all the arguments we give here. They will become the 2 parameters for the function rectangle_are()
# The arguments must have different from the parameters names: side_a -> a, side_b -> b

# REMEMBER:
# When we need that very result, we simply call the function by writing its name WITH the arguments!!
