loops = int(input())

for ch1 in range(loops):
    for ch2 in range(loops):
        for ch3 in range(loops):
            print(f'{chr(97 + ch1)}{chr(ch2 + 97)}{chr(ch3 + 97)}')