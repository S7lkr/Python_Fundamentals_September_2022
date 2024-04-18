import re

n = int(input())

for msg in range(n):
    line = input()
    pattern = r"(\D+)>(\d{3}\|[a-z]{3}\|[A-Z]{3}\|[^\<\>]{3})<\1"
    match = re.search(pattern, line)
    if match:
        password = r"[^\|]"
        message = re.findall(password, match.group(2))
        print(f"Password: {''.join(message)}")
    else:
        print(f"Try another password!")