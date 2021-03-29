T = int(input())
for i in range(T):
    tmp = int(input())
    if tmp % 4 == 0:
        print('Even')
    elif tmp % 2 == 0:
        print('Same')
    else:
        print('Odd')
