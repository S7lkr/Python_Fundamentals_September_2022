import re

# With regex-es we CAPTURE everything we need to: extract, select, replace, print, etc.
# Regex documentation: https://regex101.com/

# IMPORTANT: We group a part of regex with (): (\.[a-z]+) --> like: .com, .net, .us, .gov etc.
# beside "capturing" groups, we can create "NON-CAPTURING" groups --> (?:.......)
# These non-capturing groups are not stored as a group. They help to create our regex easier

text = "expression_92@gmail.com, webshark-77@hotmail.abv.cr.net, pesho@nh.com"
number = int(input())
regex = fr"([a-z0-{number}\-\_]+)@([a-z\-]+(?:\.\w+)*)"   # find a specific "searched value" by a given number as input



# 1. RE.SEARCH:
#
# match = re.search(regex, text)  # finds ONLY the first match it meets
# print(match)    # returns ONLY THE 1ST FOUND match as object (whole e-mail as a match) No groups in this print!
# print(match.groups())   # prints ALL GROUPS in a tuple
# print(match.group(1))   # 1st found group
# print(match.group(2))   # 2nd found group
#
# REMEMBER: if we have brackets inside of brackets: (www\.([a-z\-\.])) -> ONLY THEN we have a group(0)
# Group(0) is the group capturing everything! It is a main group -> the whole regex!



# 2. RE.MATCH:  --> Works on the same principal as re.search!
#
# matches = re.match(regex, text)
# print(matches)    # returns an object (whole regex is a match)
# print(matches.groups())     # all groups in a single match (as tuple)
#
# We can print all GROUPS like this:
# print(matches.group(1))
# print(matches.group(2))
# # OR:
# [print(match) for match in matches.groups()]



# 3. RE.FINDALL:
#
# Finds all possible matches(with the groups in it) and stores them into a list with tuples, where
# NOTE: if NO GROUPS, NO TUPLES in the list! Every match will be a simple element of the list
#
# matches = re.findall(regex, text, flags=re.IGNORECASE)  # flags are optional parameter
# print(matches)  # NOTE: every single tuple is A MATCH, and every element in it is a group!
# print(matches[2][0])    # 1st element, 3rd tuple is "pesho"



# 4. RE.FINDITER:   --> Use it to find all objects, and unpack them into matches (tuples) with groups inside
#
# NOTE: re.finditer will find every OBJECT (groups in a tuple = match)
# with all its tuples(groups)
#
matches = re.finditer(regex, text)
# print(matches)    # NOTE: returns a hashed object, which consists of as many objects as matches there are!
for match in matches:
    # print(match)    # get every OBJECT
    print(match.groups())   # get every single MATCH (regex). This is the whole e-mail
    # print(f"USERNAME: {match.group(1)}, WEBSITE: {match.group(2)}")   # 1st & 2nd group in EVERY MATCH



# 5. RE.SPLIT:  --> Same as: input().split(", ")
#
# match = re.split(", ", text)  # note that we DO NOT USE a regex. Only a separator.
# print(match)    # makes a string into a list