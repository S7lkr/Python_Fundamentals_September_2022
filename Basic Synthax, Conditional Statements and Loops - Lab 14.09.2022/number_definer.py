float_number = float(input())

if float_number == 0:
    print('zero')
elif float_number > 0:
    if float_number > 1000000:
        print('large positive')
    elif float_number < 1:
        print('small positive')
    else:
        print('positive')
else:
    # if float_number > -1:
    #     print('small negative')
    # elif float_number < -1000000:
    #     print('large negative')
    # else:
    #     print('negative')
    if abs(float_number) < 1:
        print('small negative')
    elif abs(float_number) > 1000000:
        print('large negative')
    else:
        print('negative')