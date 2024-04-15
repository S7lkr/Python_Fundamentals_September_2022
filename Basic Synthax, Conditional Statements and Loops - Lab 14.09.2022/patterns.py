# stars = int(input())
# for i in range(1, stars + 1):
#     for j in range(i):
#         print('*', end='')
#     print()
# for i in range(stars - 1, 0, -1):
#     for j in range(i):
#         print('*', end='')
#     print()

stars = int(input())

for n in range(1, stars + 1):
    print('*' * n)
for m in range(stars - 1, 0, -1):
    print('*' * m)