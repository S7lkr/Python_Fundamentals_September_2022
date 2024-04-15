text = input()
multiplier = int(input())
# Lambda is an anonymous (simple) function which can be written on a single line, instead of 'def'
formula = lambda a, b: a * b    # we read: the relation (lambda) between 'a' and 'b' is -> a * b

result = formula(text, multiplier)
print(result)
