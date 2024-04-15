def loading_progress(num):
    if num < 100:
        percent = '%' * (num//10)
        dots = '.' * (10 - num // 10)
        print(f"{num}% [{percent}{dots}]\nStill loading...")
    else:
        print('100% Complete!\n[%%%%%%%%%%]')


number = int(input())
loading_progress(number)