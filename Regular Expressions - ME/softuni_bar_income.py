import re

line = input()
total_price = 0
while line != "end of shift":
    pattern = r"%([A-Z][a-z]+)%(?:[^\$|\%|\.|\|]+)?<(\w+)>(?:[^\$|\%|\.|\|]+)?\|(\d+)\|(?:[^\$|\%|\.|\|0-9]+)?" \
              r"(\d+(?:\.\d+)?)\$"
    match = re.findall(pattern, line)
    if match:
        info = match[0]
        price = int(info[2]) * float(info[3])
        print(f"{info[0]}: {info[1]} - {price:.2f}")
        total_price += price
    line = input()
print(f"Total income: {total_price:.2f}")