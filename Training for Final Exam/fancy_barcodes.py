import re

n = int(input())
for line in range(n):
    barcode = input()
    pattern = r"@#+([A-Z][A-Za-z0-9]{4,}[A-Z])@#+"
    match = re.search(pattern, barcode)
    if match:
        digits = re.findall(r"\d", match.group(1))
        if digits:
            print(f"Product group: {''.join(digits)}")
        else:
            print("Product group: 00")
    else:
        print("Invalid barcode")