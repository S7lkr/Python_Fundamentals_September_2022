n = int(input())
text = ''
balanced = True
cnt = 1     # we set a counter, 'cnt' starting from 1, because we need to work with the first symbol, odd number

for ch in range(n):     # So, from now on, every '(' should be on an odd position, every ')' - on an even position
    symbol = input()    # On every loop, we receive a string 'symbol'
    if symbol == '(':   # if the symbol is this one: '('
        if cnt % 2 != 0:    # and ALSO '(' is on an odd position in our 'text', i.e 1st, 3rd, 5th.....
            text += symbol  # ADD IT to 'text'
            cnt += 1        # then increase the counter by 1, now cnt wil be 2, and we expect a ')'
        else:               # if the next symbol is different from ')' ....
            balanced = False    # the FLAG 'balanced' will be set from 'True' to 'False'
            break       # only in this condition the whole LOOP will BREAK, and print "UNBALANCED"
    elif symbol == ')':
        if cnt % 2 == 0:
            text += symbol
            cnt += 1
        else:
            balanced = False
            break

if balanced:
    print('BALANCED')
else:
    print('UNBALANCED')