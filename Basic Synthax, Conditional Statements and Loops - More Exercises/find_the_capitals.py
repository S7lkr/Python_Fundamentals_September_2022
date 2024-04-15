text = input()
capitols = list()
cnt = 0

for ch in text:
    cnt += 1
    if ch.isupper():
        for i in range(cnt-1, -1, -1):
            capitols.append(i)
            break
print(capitols)