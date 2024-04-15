numbers = list(map(int, input().split(', ')))

positive = list(filter(lambda x: x >= 0, numbers))
negative = list(filter(lambda y: y < 0, numbers))
even = list(filter(lambda z: z % 2 == 0, numbers))
odd = list(filter(lambda num: num % 2 != 0, numbers))

print(f"Positive: {', '.join(map(str, positive))}")
print(f"Negative: {', '.join(map(str, negative))}")
print(f"Even: {', '.join(map(str, even))}")
print(f"Odd: {', '.join(map(str, odd))}")