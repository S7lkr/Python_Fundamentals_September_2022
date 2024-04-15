electrons = int(input())
shells = []
shell_cnt = 1

while 2 * pow(shell_cnt, 2) <= electrons:
    electrons_in_shell = 2 * pow(shell_cnt, 2)
    electrons -= electrons_in_shell
    shells.append(electrons_in_shell)
    shell_cnt += 1
else:
    if electrons > 0:
        shells.append(electrons)
print(shells)