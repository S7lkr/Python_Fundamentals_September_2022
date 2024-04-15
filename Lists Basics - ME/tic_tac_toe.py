def vertical_check(r1):
    if row1[index] == 1:
        return "First player wins"
    return "Second player won"


def horizontal_check(r1):
    if 0 not in row:
        if sum(row) == 3:
            return "First player won"
        elif sum(row) == 6:
            return "Second player won"
    return False


def diagonals_check(r1, r2, r3):
    if row1[0] == row2[1] == row3[2] == 1 or row1[2] == row2[1] == row3[0] == 1:
        return "First player won"
    elif row1[0] == row2[1] == row3[2] == 2 or row1[2] == row2[1] == row3[0] == 2:
        return "Second player won"
    return False


row1 = list(map(int, input().split()))
row2 = list(map(int, input().split()))
row3 = list(map(int, input().split()))
grid = [row1, row2, row3]

for index in range(3):
    if (row1[index] == row2[index] == row3[index]) != 0:
        print(vertical_check(row1))
        break
    row = grid[index]
    if horizontal_check(row1):
        print(horizontal_check(row1))
        break
    if row2[1] != 0:
        if diagonals_check(row1, row2, row3):
            print(diagonals_check(row1, row2, row3))
            break
else:
    print("Draw!")