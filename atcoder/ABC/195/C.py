import sys

n, m, q = map(int, sys.stdin.buffer.readline().split())
wv = [list(map(int, sys.stdin.buffer.readline().split())) for _ in range(n)]
wv.sort(key=lambda x: x[1], reverse=True)
x = list(map(int, sys.stdin.buffer.readline().split()))
for z in sys.stdin.buffer.readlines():
    l, r = map(int, z.split())
    ans = [0] * m
    cwv = wv[:]
    cx = x[:]
    for i in range(l-1, r):
        cx[i] = 0
    cx.sort()
    for j in range(n):
        for i in range(m):
            if cwv[j][0] <= cx[i] and ans[i] < cwv[j][1]:
                ans[i] = cwv[j][1]
                break
    print(sum(ans))
