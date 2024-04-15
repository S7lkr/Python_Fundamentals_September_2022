def calculate(act, n1, n2):
    if act == 'add':
        return n1 + n2
    elif act == 'subtract':
        return n1 - n2
    elif act == 'multiply':
        return n1 * n2
    elif act == 'divide':
        return int(n1 / n2)


operation = input()
num1 = int(input())
num2 = int(input())
print(calculate(operation, num1, num2))