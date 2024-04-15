def data_type(type, text):
    if type == 'int':
        text = int(text) * 2
        return text
    elif type == 'real':
        text = float(text) * 1.5
        return f'{text:.2f}'
    return f'${text}$'


some_type = input()
text_or_num = input()
print(data_type(some_type, text_or_num))