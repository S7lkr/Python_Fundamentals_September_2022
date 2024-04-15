import re

html_code = input()
title_pattern = r"<title>([A-Za-z0-9\s]+)</title>"
content_pattern = r">([^\>\<]+)<"
title = re.search(title_pattern, html_code)

print(f"Title: {title.group(1)}")

content = re.findall(content_pattern, html_code)
result = "".join(content)
result = result.replace(title.group(1), "")
result = result.replace("\\n", "")

print(f"Content: {result}")