import re

# also works --> (?<![-_.])(\b[a-z0-9]+[a-z0-9\.\-\_]*@[a-z0-9-]+[a-z0-9-\.]*\.[a-z0-9]+)\b
pattern = r"\s([a-z0-9]+[a-z0-9\_\-\.]*@[a-z0-9]+[a-z0-9\-]*[\w+\.]*\.\w+)\b"
sentence = input()
emails = re.findall(pattern, sentence)
print("\n".join(emails))