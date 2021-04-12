import math
R, X, Y = map(int, input().split())
tmp = pow(X ** 2 + Y ** 2, 0.5)
if tmp == R:
    print(1)
elif tmp <= 2*R:
    print(2)
else:
    print(math.ceil(tmp/R))
