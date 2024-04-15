words = input().split()
palindrome = input()
cnt = 0
palindromes = []

for word in words:
    if word == word[::-1]:  # OR we can write: if word == ''.join(reversed(word)):
        palindromes.append(word)
    if word == palindrome:
        cnt += 1

print(palindromes)
print(f"Found palindrome {cnt} times")