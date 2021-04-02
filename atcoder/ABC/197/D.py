import math


def rotate(x1, n, mid):
    x1[0] -= xmid[0]
    x1[1] -= xmid[1]
    angle = 2 * math.pi / n

    xrotate = math.cos(angle) * x1[0] - math.sin(angle) * x1[1]
    yrotate = math.sin(angle) * x1[0] + math.cos(angle) * x1[1]

    return [xrotate+xmid[0], yrotate+xmid[1]]


n = int(input())

x0 = list(map(int, input().split()))
x2 = list(map(int, input().split()))

xmid = [(x0[0] + x2[0]) / 2, (x0[1] + x2[1]) / 2]

ans = rotate(x0, n, xmid)
print(ans[0], ans[1])
