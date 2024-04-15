key = int(input())
symbols = int(input())
message = ''

for sym in range(symbols):
    symbol = ord(input()) + key
    symbol = chr(symbol)
    message += symbol
print(message)
