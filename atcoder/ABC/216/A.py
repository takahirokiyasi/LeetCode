import math
tmp = float(input())
tmp = int(tmp * 10)
y = tmp % 10
x = math.floor(tmp / 10)

if 0 <= y <= 2:
    print(str(x) + '-')
elif 3 <= y <= 6:
    print(str(x))
else:
    print(str(x) + '+')
