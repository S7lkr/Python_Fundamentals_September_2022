number = list(map(int, input().split()))

# The filter() b/i func. extracts elements from an iterable (list, tuple, set etc.), for which a function returns True.
# filter() will return a value ONLY IF lambda func. have checked it and said True (condition)
# Lambda func. returns True for even numbers. Hence, the filter() returns an iterator containing even numbers only
only_even = filter(lambda digit: (digit % 2 == 0), number)

print(list(only_even))