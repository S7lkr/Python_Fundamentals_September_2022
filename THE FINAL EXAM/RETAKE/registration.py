import re

number_of_lines = int(input())
cnt = 0
for line in range(number_of_lines):
    text = input()
    pattern = r"U\$([A-Z][a-z]{2,})U\$P@\$([a-zA-Z]{5,}\d+)P@\$"
    match = re.search(pattern, text)
    if match:
        cnt += 1
        username = match.group(1)
        password = match.group(2)
        print(f"Registration was successful\nUsername: {username}, Password: {password}")
    else:
        print("Invalid username or password")
print(f"Successful registrations: {cnt}")