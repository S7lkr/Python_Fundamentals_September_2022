import re

valid_urls = []
line = input()
while line:
    pattern = r"(w{3}\.[A-Za-z0-9\-\.]+\.[a-z]+)"
    website = re.search(pattern, line)
    if website:
        valid_urls.append(website.group(1))
    line = input()
print('\n'.join(valid_urls))

# import re
#
# pattern = r"(w{3}\.[a-zA-Z0-9\-]+[a-z\.\-]*\.[a-z]+)"
# line = input()
# while line:
#     website = re.search(pattern, line)
#     if website:
#         print(website.group(1))
#     line = input()